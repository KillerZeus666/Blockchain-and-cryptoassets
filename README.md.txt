Proyecto Final NFT – ChessNFT
📌 Descripción

Este proyecto implementa un sistema de NFTs basado en el estándar ERC-721, desplegado en la red de pruebas Ethereum Sepolia.

El contrato inteligente permite la creación, gestión y comercialización de NFTs asociados a partidas de un sistema de juego, con soporte para almacenamiento descentralizado mediante IPFS y pagos mediante un token ERC20 personalizado.

⚙️ Tecnologías utilizadas
Solidity 
Remix IDE
MetaMask
Ethereum Sepolia Testnet
OpenZeppelin (ERC-721)
IPFS (almacenamiento descentralizado)

📜 Contratos desplegados
🧩 NFT Contract (ChessNFT)
Red: Sepolia Ethereum
Dirección del contrato:
0xacf183288038FB082541f266BaF8B461319FEFF0
💰 Token de pago (ERC20 PUJ26i)
0x80bF8e5293b241Cf8810671eDBb049a5F3194230
🎯 Funcionalidades del contrato
Mint de NFTs mediante mintGame()
Asociación de metadata mediante IPFS
Compra de NFTs usando token ERC20
Listado de NFTs en venta (putOnSale)
Transferencia y gestión de propiedad
Consulta de información del NFT
🌐 Enlaces IPFS (Metadata de partidas)
Juego 1: ipfs://bafkreihh4a4snjvjf4cvuocj2ucdxk6fkyuaatcqe4eeu4vg5flfzkhvhu
Juego 2: ipfs://bafkreiacmaymsi4yj6exlqtqovtyjasmldhp7bk3sehmsulz5xvhmjnkwe
Juego 3: ipfs://bafkreiapsslxuwvp4gfb37w3teiysoixedaqy3ysbe5bokrxysidotnhoa
Juego 4: ipfs://bafkreifegonmt2zfyql5vwg2khtyn5qywtoaygyxawb55gzip4xrkwqopq
Juego 5: ipfs://bafkreih7lnjvcb3jnmcb2cwww5vhza5qizy63ehvwtw4skhadho3o2fyc4
🧾 ABI del contrato

El ABI del contrato ERC-721 se encuentra incluido en el repositorio dentro del archivo:

abi.json
🚀 Cómo interactuar con el contrato
Abrir Remix IDE
Conectar MetaMask en la red Sepolia
Seleccionar Injected Provider – MetaMask

Importar el contrato usando la dirección:

0xacf183288038FB082541f266BaF8B461319FEFF0
Ejecutar funciones como:
mintGame(_tokenURI)
putOnSale(tokenId, price)
buyNFT(tokenId)
tokenURI(tokenId)
👩‍💻 Autor

Katheryn Guasca. 
Proyecto desarrollado como entrega final de curso sobre Blockchain.

📦 Estructura del proyecto
ProyectoFinal_Guasca_Katheryn.zip
│
├── direccionContrato.txt
├──ABI.json
├── README.md
├── ChessNFT.sol
└── ipfs_links.txt