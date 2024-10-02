const { ethers } = require(«ethers»);

async function massTransfer(recipients, amount) {
    const provider = new ethers.providers.JsonRpcProvider(«YOUR_RPC_URL»);
    const wallet = new ethers.Wallet(«YOUR_PRIVATE_KEY», provider);
    const contract = new ethers.Contract(«CONTRACT_ADDRESS», abi, wallet);

    const tx = await contract.massTransfer(recipients, amount);
    await tx.wait();
    console.log(«The tokens have been transferred!»);
}
