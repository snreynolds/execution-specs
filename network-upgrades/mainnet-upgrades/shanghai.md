## Shanghai Network Upgrade Specification

### Included EIPs
Changes included in the Network Upgrade.

* [EIP-3651: Warm COINBASE](https://eips.ethereum.org/EIPS/eip-3651)
* [EIP-3855: PUSH0 instruction](https://eips.ethereum.org/EIPS/eip-3855)
* [EIP-3860: Limit and meter initcode](https://eips.ethereum.org/EIPS/eip-3860)
* [EIP-4895: Beacon chain push withdrawals as operations](https://eips.ethereum.org/EIPS/eip-4895)

### EIPs Considered for Inclusion
Changes [Considered for Inclusion](https://github.com/ethereum/execution-specs/tree/master/network-upgrades#definitions) as part of this upgrade, or potentially future ones. 

* [EIP-1153: Transient storage opcodes](https://eips.ethereum.org/EIPS/eip-1153)
* [EIP-2537: Precompile for BLS12-381 curve operations](https://eips.ethereum.org/EIPS/eip-2537)
* [EIP-3540: EVM Object Format (EOF) v1](https://eips.ethereum.org/EIPS/eip-3540)
* [EIP-3670: EOF - Code Validation](https://eips.ethereum.org/EIPS/eip-3670)
* [EIP-4200: EOF - Static relative jumps](https://eips.ethereum.org/EIPS/eip-4200)
* [EIP-4750: EOF - Functions](https://eips.ethereum.org/EIPS/eip-4750)
* [EIP-4844: Shard Blob Transactions](https://eips.ethereum.org/EIPS/eip-4844)
* [EIP-5450: EOF - Stack Validation](https://eips.ethereum.org/EIPS/eip-5450)

### Readiness Checklist

**List of outstanding items before deployment.**

Code merged into Participating Clients:


| EIP | [EIP-1153](https://eips.ethereum.org/EIPS/eip-1153) | [EIP-3540](https://eips.ethereum.org/EIPS/eip-3540) | [EIP-3651](https://eips.ethereum.org/EIPS/eip-3651) | [EIP-3670](https://eips.ethereum.org/EIPS/eip-3670) | [EIP-3855](https://eips.ethereum.org/EIPS/eip-3855) | [EIP-3860](https://eips.ethereum.org/EIPS/eip-3860) | [EIP-4895](https://eips.ethereum.org/EIPS/eip-4895) |
|------|------|------|------|------|------|------|------|
| **Geth**         | [Merged](https://github.com/ethereum/go-ethereum/pull/26003) | [Not merged](https://github.com/ethereum/go-ethereum/pull/22958) | [Merged](https://github.com/ethereum/go-ethereum/pull/25819) | [Not merged](https://github.com/ethereum/go-ethereum/pull/24090) | [Merged](https://github.com/ethereum/go-ethereum/pull/24039) | [Not merged](https://github.com/ethereum/go-ethereum/pull/23847) | [Not merged](https://github.com/ethereum/go-ethereum/pull/25838) |
| **Besu**         | [Not merged](https://github.com/hyperledger/besu/pull/4118) | [Merged](https://github.com/hyperledger/besu/pull/4644) | [Merged](https://github.com/hyperledger/besu/pull/4620) | [Merged](https://github.com/hyperledger/besu/pull/4644) | [Merged](https://github.com/hyperledger/besu/pull/4660) | | [Not merged](https://github.com/hyperledger/besu/pull/4552)|
| **Nethermind**   | [Merged](https://github.com/NethermindEth/nethermind/pull/4126) | [Not merged](https://github.com/NethermindEth/nethermind/pull/4608)| [Merged](https://github.com/NethermindEth/nethermind/pull/4594)|[Not merged](https://github.com/NethermindEth/nethermind/pull/4609)|[Merged](https://github.com/NethermindEth/nethermind/pull/4599) |[Merged](https://github.com/NethermindEth/nethermind/pull/4740) |[Not merged](https://github.com/NethermindEth/nethermind/pull/4731) |
| **Erigon**       | | | [Merged](https://github.com/ledgerwatch/erigon/pull/5745) | | [Merged](https://github.com/ledgerwatch/erigon/pull/5256) | [Merged](https://github.com/ledgerwatch/erigon/pull/5892) | [Not merged](https://github.com/ledgerwatch/erigon/pull/6009) |
| **EthereumJS**   | [Merged](https://github.com/ethereumjs/ethereumjs-monorepo/pull/1860) | [Merged](https://github.com/ethereumjs/ethereumjs-monorepo/pull/1719) | [Merged](https://github.com/ethereumjs/ethereumjs-monorepo/pull/1814) | [Merged](https://github.com/ethereumjs/ethereumjs-monorepo/pull/1743) | [Merged](https://github.com/ethereumjs/ethereumjs-monorepo/pull/1616) | [Merged](https://github.com/ethereumjs/ethereumjs-monorepo/pull/1619) | [Merged](https://github.com/ethereumjs/ethereumjs-monorepo/pull/2353) |

 Tasks
- [ ] Client Integration Testing
  - [ ] Deploy a Client Integration Testnet
  - [ ] Integration Tests
  - [ ] Fuzz Testing
 - [ ] Select Fork Blocks
 - [ ] Deploy Clients
   - [ ]  Geth
   - [ ]  Besu
   - [ ]  Nethermind
   - [ ]  OpenEthereum
   - [ ]  Erigon
   - [ ]  EthereumJS
 - [ ] Pass Fork Blocks
