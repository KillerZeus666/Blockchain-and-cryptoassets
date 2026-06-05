// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract ChessNFT is ERC721URIStorage, Ownable {

    IERC20 public paymentToken;

    uint256 public nextTokenId;

    struct Sale {
        address seller;
        uint256 price;
        bool onSale;
    }

    mapping(uint256 => Sale) public sales;

    constructor(address _paymentToken)
        ERC721("ChessNFT", "CHESS")
        Ownable(msg.sender)
    {
        paymentToken = IERC20(_paymentToken);
    }

    function mintGame(string memory _tokenURI) public {

        uint256 tokenId = nextTokenId;

        _safeMint(msg.sender, tokenId);

        _setTokenURI(tokenId, _tokenURI);

        nextTokenId++;
    }

    function putOnSale(uint256 tokenId, uint256 price) public {

        require(ownerOf(tokenId) == msg.sender, "Not owner");

        sales[tokenId] = Sale({
            seller: msg.sender,
            price: price,
            onSale: true
        });
    }

    function getSaleInfo(uint256 tokenId)
        public
        view
        returns(address, uint256, bool)
    {
        Sale memory s = sales[tokenId];

        return (s.seller, s.price, s.onSale);
    }

    function buyNFT(uint256 tokenId) public {

        Sale memory s = sales[tokenId];

        require(s.onSale, "Not for sale");

        paymentToken.transferFrom(
            msg.sender,
            s.seller,
            s.price
        );

        _transfer(s.seller, msg.sender, tokenId);

        sales[tokenId].onSale = false;
    }
}