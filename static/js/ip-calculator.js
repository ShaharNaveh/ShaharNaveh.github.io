function calculateSubnet() {
    let ip = document.getElementById("ip-address").value;
    let subnet = document.getElementById("subnet-mask").value;
    
    // Convert IP and subnet to binary
    let ipBin = ip.split('.').map(Number).map(num => num.toString(2).padStart(8, '0')).join('');
    let subnetBin = subnet.split('.').map(Number).map(num => num.toString(2).padStart(8, '0')).join('');
    
    // Calculate network and broadcast addresses
    let networkAddressBin = ipBin.substring(0, subnetBin.indexOf('0')).padEnd(32, '0');
    let broadcastAddressBin = ipBin.substring(0, subnetBin.indexOf('0')).padEnd(32, '1');
    
    let networkAddress = networkAddressBin.match(/.{1,8}/g).map(bin => parseInt(bin, 2)).join('.');
    let broadcastAddress = broadcastAddressBin.match(/.{1,8}/g).map(bin => parseInt(bin, 2)).join('.');
    
    // Display results
    document.getElementById("result").innerHTML = `
        <p>Network Address: ${networkAddress}</p>
        <p>Broadcast Address: ${broadcastAddress}</p>
    `;
}
