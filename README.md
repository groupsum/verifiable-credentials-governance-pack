<div align="center">

<h1>verifiable-credentials-governance-pack</h1>

<p>
  <a href="https://pypi.org/project/verifiable-credentials-governance-pack/"><img alt="PyPI version" src="https://img.shields.io/pypi/v/verifiable-credentials-governance-pack.svg"></a>
  <a href="https://pepy.tech/projects/verifiable-credentials-governance-pack"><img alt="Downloads" src="https://static.pepy.tech/badge/verifiable-credentials-governance-pack"></a>
  <a href="https://hits.sh/github.com/groupsum/verifiable-credentials-governance-pack/"><img alt="Hits" src="https://hits.sh/github.com/groupsum/verifiable-credentials-governance-pack.svg"></a>
  <a href="https://pypi.org/project/verifiable-credentials-governance-pack/"><img alt="Python versions" src="https://img.shields.io/pypi/pyversions/verifiable-credentials-governance-pack.svg"></a>
  <a href="https://github.com/groupsum/verifiable-credentials-governance-pack/blob/master/LICENSE"><img alt="License" src="https://img.shields.io/pypi/l/verifiable-credentials-governance-pack.svg"></a>
  <a href="https://github.com/groupsum/verifiable-credentials-governance-pack/actions/workflows/ci.yml"><img alt="CI" src="https://github.com/groupsum/verifiable-credentials-governance-pack/actions/workflows/ci.yml/badge.svg?branch=master"></a>
</p>

<p>
  <a href="https://github.com/groupsum/verifiable-credentials-governance-pack"><img alt="GitHub repo" src="https://img.shields.io/badge/GitHub-groupsum%2Fverifiable--credentials--governance--pack-181717?logo=github"></a>
</p>

</div>

`verifiable-credentials-governance-pack` is an SSOT Registry pack for W3C Verifiable Credentials, verifiable presentations, securing mechanisms, status models, schema use, cryptosuite profiles, selective disclosure profile boundaries, and adjacent issuance/presentation protocols.

It gives product, platform, identity, wallet, issuer, verifier, and compliance teams a reusable ADR/SPEC starting point for repositories that need to govern credential data model support, presentation processing, Data Integrity proofs, JOSE/COSE securing, status and revocation mechanisms, schema and vocabulary usage, OpenID4VC protocol boundaries, and selective-disclosure format claims.

## What Is An SSOT Registry Pack?

An SSOT Registry pack is an installable package of governed Architecture Decision Records (ADRs) and Specifications (SPECs) for [`ssot-registry`](https://pypi.org/project/ssot-registry/). The pack supplies reusable decision and requirement documents that downstream repositories can synchronize into their local `.ssot` registry and link to features, tests, claims, evidence, and releases.

This makes governance portable. A project can adopt the pack, synchronize the documents, list the active requirements, and connect local implementation or test work to the shared IDs.

## Why This Pack Exists

Verifiable Credentials governance crosses data model semantics, proof formats, presentation processing, credential status, cryptographic suites, schema and vocabulary policy, wallet and issuer protocols, and interoperability claim language. Teams need stable decisions and requirements before claiming support for a VC format, securing mechanism, issuance flow, presentation flow, or selective disclosure profile.

This pack helps teams:

- apply reviewed VC governance requirements across projects
- distinguish VC core data model requirements from optional DID and OpenID4VC integrations
- keep Data Integrity, JOSE/COSE, status, schema, cryptosuite, and presentation requirements explicit
- give issuer, verifier, wallet, platform, compliance, and implementation teams stable ADR and SPEC IDs
- connect downstream features, tests, claims, evidence, and releases to shared governance records

## Pack Metadata

- Pack ID: `pack:verifiable-credentials-governance`
- PyPI package: `verifiable-credentials-governance-pack`
- Import package: `verifiable_credentials_governance_pack`
- GitHub repository: [groupsum/verifiable-credentials-governance-pack](https://github.com/groupsum/verifiable-credentials-governance-pack)
- Reservation owner: `extension-pack:verifiable-credentials-governance-pack`

## Domain Focus

The pack focuses on domains where VC behavior affects interoperability, security review, product claims, and release evidence:

- W3C Verifiable Credentials Data Model and verifiable presentation semantics
- Data Integrity and JOSE/COSE securing mechanism boundaries
- credential status, suspension, and revocation requirements
- JSON Schema, vocabulary, and validation policy
- EdDSA, ECDSA, BBS, and future cryptosuite profile governance
- OpenID4VCI, OpenID4VP, SIOPv2, and OpenID Federation adjacency
- DIF Presentation Exchange and SD-JWT VC boundary handling
- optional DID identifier integration without making DIDs a baseline VC prerequisite

## Authority Sources

Core VC authorities:

- [W3C Verifiable Credentials Data Model v2.0](https://www.w3.org/TR/vc-data-model-2.0/)
- [W3C Verifiable Credential Data Integrity 1.0](https://www.w3.org/TR/vc-data-integrity/)
- [W3C Securing Verifiable Credentials using JOSE and COSE](https://www.w3.org/TR/vc-jose-cose/)
- [W3C Bitstring Status List v1.0](https://www.w3.org/TR/vc-bitstring-status-list/)
- [W3C Verifiable Credentials JSON Schema](https://www.w3.org/TR/vc-json-schema/)

Cryptosuite authorities:

- [Data Integrity EdDSA Cryptosuites v1.0](https://www.w3.org/TR/vc-di-eddsa/)
- [Data Integrity ECDSA Cryptosuites v1.0](https://www.w3.org/TR/vc-di-ecdsa/)
- [Data Integrity BBS Cryptosuites v1.0](https://www.w3.org/TR/vc-di-bbs/)

Adjacent protocol and profile authorities:

- [OpenID for Verifiable Credential Issuance](https://openid.net/specs/openid-4-verifiable-credential-issuance-1_0.html)
- [OpenID for Verifiable Presentations](https://openid.net/specs/openid-4-verifiable-presentations-1_0.html)
- [Self-Issued OpenID Provider v2](https://openid.net/specs/openid-connect-self-issued-v2-1_0.html)
- [OpenID Federation](https://openid.net/specs/openid-federation-1_0.html)

Identifier dependencies:

- [W3C DID Core](https://www.w3.org/TR/did-core/)
- [W3C Controlled Identifiers](https://www.w3.org/TR/cid/)
- [W3C DID Extensions](https://www.w3.org/TR/did-spec-registries/)

Watchlist-only adjacent sources:

- DIF Presentation Exchange
- DIF Credential Manifest
- SD-JWT VC
- Token Status List and JWT/CWT Status List drafts
- RFC 9396 Rich Authorization Requests
- RFC 8414 Authorization Server Metadata
- EUDI ARF
- Open Badges 3.0
- W3C Traceability Vocabulary

## Included ADRs

- [`adr:verifiable-credentials-are-attestable-claims-not-local-authentication-credentials`](https://github.com/groupsum/verifiable-credentials-governance-pack/blob/master/src/verifiable_credentials_governance_pack/templates/adr/ADR-1000-verifiable-credentials-are-attestable-claims-not-local-authentication-credentials.yaml) - Verifiable Credentials Are Attestable Claims Not Local Authentication Credentials
- [`adr:w3c-vc-data-model-is-the-core-credential-and-presentation-authority`](https://github.com/groupsum/verifiable-credentials-governance-pack/blob/master/src/verifiable_credentials_governance_pack/templates/adr/ADR-1001-w3c-vc-data-model-is-the-core-credential-and-presentation-authority.yaml) - W3C VC Data Model Is The Core Credential And Presentation Authority
- [`adr:vc-securing-mechanisms-are-profiled-as-data-integrity-and-jose-cose`](https://github.com/groupsum/verifiable-credentials-governance-pack/blob/master/src/verifiable_credentials_governance_pack/templates/adr/ADR-1002-vc-securing-mechanisms-are-profiled-as-data-integrity-and-jose-cose.yaml) - VC Securing Mechanisms Are Profiled As Data Integrity And JOSE COSE
- [`adr:vc-status-and-revocation-are-governed-through-explicit-status-mechanisms`](https://github.com/groupsum/verifiable-credentials-governance-pack/blob/master/src/verifiable_credentials_governance_pack/templates/adr/ADR-1003-vc-status-and-revocation-are-governed-through-explicit-status-mechanisms.yaml) - VC Status And Revocation Are Governed Through Explicit Status Mechanisms
- [`adr:dids-are-optional-identifiers-for-vc-not-a-vc-prerequisite`](https://github.com/groupsum/verifiable-credentials-governance-pack/blob/master/src/verifiable_credentials_governance_pack/templates/adr/ADR-1004-dids-are-optional-identifiers-for-vc-not-a-vc-prerequisite.yaml) - DIDs Are Optional Identifiers For VC Not A VC Prerequisite
- [`adr:openid4vc-protocols-are-transport-rails-not-vc-core`](https://github.com/groupsum/verifiable-credentials-governance-pack/blob/master/src/verifiable_credentials_governance_pack/templates/adr/ADR-1005-openid4vc-protocols-are-transport-rails-not-vc-core.yaml) - OpenID4VC Protocols Are Transport Rails Not VC Core
- [`adr:selective-disclosure-and-format-profiles-must-be-explicitly-declared`](https://github.com/groupsum/verifiable-credentials-governance-pack/blob/master/src/verifiable_credentials_governance_pack/templates/adr/ADR-1006-selective-disclosure-and-format-profiles-must-be-explicitly-declared.yaml) - Selective Disclosure And Format Profiles Must Be Explicitly Declared

## Included SPECs

- [`spc:verifiable-credential-data-model-contract`](https://github.com/groupsum/verifiable-credentials-governance-pack/blob/master/src/verifiable_credentials_governance_pack/templates/specs/SPEC-2000-verifiable-credential-data-model-contract.yaml) - Verifiable Credential Data Model Contract
- [`spc:verifiable-presentation-processing-contract`](https://github.com/groupsum/verifiable-credentials-governance-pack/blob/master/src/verifiable_credentials_governance_pack/templates/specs/SPEC-2001-verifiable-presentation-processing-contract.yaml) - Verifiable Presentation Processing Contract
- [`spc:vc-data-integrity-proof-contract`](https://github.com/groupsum/verifiable-credentials-governance-pack/blob/master/src/verifiable_credentials_governance_pack/templates/specs/SPEC-2002-vc-data-integrity-proof-contract.yaml) - VC Data Integrity Proof Contract
- [`spc:vc-jose-cose-securing-contract`](https://github.com/groupsum/verifiable-credentials-governance-pack/blob/master/src/verifiable_credentials_governance_pack/templates/specs/SPEC-2003-vc-jose-cose-securing-contract.yaml) - VC JOSE COSE Securing Contract
- [`spc:vc-status-and-revocation-contract`](https://github.com/groupsum/verifiable-credentials-governance-pack/blob/master/src/verifiable_credentials_governance_pack/templates/specs/SPEC-2004-vc-status-and-revocation-contract.yaml) - VC Status And Revocation Contract
- [`spc:vc-json-schema-and-vocabulary-contract`](https://github.com/groupsum/verifiable-credentials-governance-pack/blob/master/src/verifiable_credentials_governance_pack/templates/specs/SPEC-2005-vc-json-schema-and-vocabulary-contract.yaml) - VC JSON Schema And Vocabulary Contract
- [`spc:vc-cryptosuite-profile-contract`](https://github.com/groupsum/verifiable-credentials-governance-pack/blob/master/src/verifiable_credentials_governance_pack/templates/specs/SPEC-2006-vc-cryptosuite-profile-contract.yaml) - VC Cryptosuite Profile Contract
- [`spc:openid4vci-issuance-boundary-contract`](https://github.com/groupsum/verifiable-credentials-governance-pack/blob/master/src/verifiable_credentials_governance_pack/templates/specs/SPEC-2007-openid4vci-issuance-boundary-contract.yaml) - OpenID4VCI Issuance Boundary Contract
- [`spc:openid4vp-presentation-boundary-contract`](https://github.com/groupsum/verifiable-credentials-governance-pack/blob/master/src/verifiable_credentials_governance_pack/templates/specs/SPEC-2008-openid4vp-presentation-boundary-contract.yaml) - OpenID4VP Presentation Boundary Contract
- [`spc:dif-presentation-exchange-boundary-contract`](https://github.com/groupsum/verifiable-credentials-governance-pack/blob/master/src/verifiable_credentials_governance_pack/templates/specs/SPEC-2009-dif-presentation-exchange-boundary-contract.yaml) - DIF Presentation Exchange Boundary Contract
- [`spc:sd-jwt-vc-and-token-status-list-boundary-contract`](https://github.com/groupsum/verifiable-credentials-governance-pack/blob/master/src/verifiable_credentials_governance_pack/templates/specs/SPEC-2010-sd-jwt-vc-and-token-status-list-boundary-contract.yaml) - SD-JWT VC And Token Status List Boundary Contract

## Install With uv

Install the pack into a project environment:

```bash
uv add verifiable-credentials-governance-pack
```

Install it alongside the SSOT Registry CLI:

```bash
uv add ssot-registry verifiable-credentials-governance-pack
```

Run without adding dependencies to a project:

```bash
uvx --from ssot-registry --with verifiable-credentials-governance-pack ssot --help
```

## Install With The SSOT Registry Pack CLI

Pack-enabled SSOT Registry environments can inspect, preflight, and synchronize packs through the pack command surface:

```bash
uv run ssot pack inspect verifiable_credentials_governance_pack
uv run ssot pack preflight . verifiable_credentials_governance_pack --all
uv run ssot pack sync . verifiable_credentials_governance_pack --all --trust --yes
```

## Use With The SSOT Registry CLI

After the pack is installed in the same environment as `ssot-registry`, validate the synchronized governance surface:

```bash
uv run ssot validate .
uv run ssot adr list .
uv run ssot spec list .
uv run ssot spec get . --id spc:pack.verifiable-credentials-governance.verifiable-credential-data-model-contract
```

Use the IDs from this pack when linking project features, tests, claims, and release evidence in your local `.ssot` registry.

## Programmatic Usage

```python
from verifiable_credentials_governance_pack import load_document_manifest, read_packaged_document_text

adr_manifest = load_document_manifest("adr")
spec_manifest = load_document_manifest("spec")

print(adr_manifest[0]["id"])
print(spec_manifest[0]["id"])

text = read_packaged_document_text("spec", "SPEC-2000-verifiable-credential-data-model-contract.yaml")
print(text[:120])
```

## Resources

- GitHub repository: [groupsum/verifiable-credentials-governance-pack](https://github.com/groupsum/verifiable-credentials-governance-pack)
- PyPI package: [verifiable-credentials-governance-pack](https://pypi.org/project/verifiable-credentials-governance-pack/)
- SSOT Registry: [ssot-registry](https://pypi.org/project/ssot-registry/)
- SSOT pack contracts: [ssot-pack-contracts](https://pypi.org/project/ssot-pack-contracts/)
