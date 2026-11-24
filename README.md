# verifiable-credentials-governance-pack

<!-- readme-standards:begin branding -->
<p align="center"><a href="https://github.com/groupsum/readme-standards"><img src="https://raw.githubusercontent.com/groupsum/readme-standards/master/docs/assets/readme-standards.svg" alt="Groupsum README Standards" width="300"></a></p>
<p align="center"><strong>verifiable-credentials-governance-pack</strong></p>
<p align="center">Installable SSOT governance pack for W3C Verifiable Credentials, presentations, securing mechanisms, status models, schema use, cryptosuite profiles, and adjacent issuance/presentation protocols.</p>
<p align="center">
<a href="https://pypi.org/project/verifiable-credentials-governance-pack/"><img alt="pypi: verifiable-credentials-governance-pack unpublished" src="https://img.shields.io/static/v1?label=pypi&amp;message=verifiable-credentials-governance-pack%20unpublished&amp;labelColor=1E293B&amp;color=92400E"></a>
<a href="https://github.com/groupsum/verifiable-credentials-governance-pack/blob/master/pyproject.toml"><img alt="Source version: 0.2.0.dev1" src="https://img.shields.io/static/v1?label=Source%20version&amp;message=0.2.0.dev1&amp;labelColor=1E293B&amp;color=4338CA"></a>
<a href="https://github.com/groupsum/verifiable-credentials-governance-pack/blob/master/pyproject.toml"><img alt="Python: &gt;=3.10,&lt;3.15" src="https://img.shields.io/static/v1?label=Python&amp;message=%3E%3D3.10%2C%3C3.15&amp;labelColor=1E293B&amp;color=0F766E"></a>
<a href="https://github.com/groupsum/verifiable-credentials-governance-pack/blob/master/pyproject.toml"><img alt="Layer: governance" src="https://img.shields.io/static/v1?label=Layer&amp;message=governance&amp;labelColor=1E293B&amp;color=6D28D9"></a>
<a href="https://github.com/groupsum/verifiable-credentials-governance-pack/blob/master/README.md#lifecycle-and-migration"><img alt="Lifecycle: active" src="https://img.shields.io/static/v1?label=Lifecycle&amp;message=active&amp;labelColor=1E293B&amp;color=166534"></a>
<a href="https://github.com/groupsum/verifiable-credentials-governance-pack/blob/master/LICENSE"><img alt="License: Apache-2.0" src="https://img.shields.io/static/v1?label=License&amp;message=Apache-2.0&amp;labelColor=1E293B&amp;color=86198F"></a>
<a href="https://github.com/groupsum/verifiable-credentials-governance-pack/blob/master/README.md#notices"><img alt="Notice: not required" src="https://img.shields.io/static/v1?label=Notice&amp;message=not%20required&amp;labelColor=1E293B&amp;color=475569"></a>
</p>
<p align="center">
<a href="https://pypi.org/project/verifiable-credentials-governance-pack/"><img alt="pypi downloads: verifiable-credentials-governance-pack: unpublished" src="https://img.shields.io/static/v1?label=pypi%20downloads&amp;message=verifiable-credentials-governance-pack%3A%20unpublished&amp;labelColor=1E293B&amp;color=92400E"></a>
<a href="https://github.com/groupsum/verifiable-credentials-governance-pack/blob/master/README.md"><img alt="README hits: verifiable-credentials-governance-pack" src="https://hits.sh/github.com/groupsum/verifiable-credentials-governance-pack/README.md.svg?label=README%20hits&amp;labelColor=1E293B&amp;color=0E7490"></a>
</p>
<p align="center">
<a href="https://github.com/groupsum/verifiable-credentials-governance-pack/actions/workflows/readme-standards.yml"><img alt="README standards: CI gate" src="https://img.shields.io/static/v1?label=README%20standards&amp;message=CI%20gate&amp;labelColor=1E293B&amp;color=1D4ED8"></a>
<a href="https://github.com/groupsum/verifiable-credentials-governance-pack/actions/workflows/readme-standards.yml"><img alt="Tests: package and example checks" src="https://img.shields.io/static/v1?label=Tests&amp;message=package%20and%20example%20checks&amp;labelColor=1E293B&amp;color=0F766E"></a>
<a href="https://github.com/groupsum/verifiable-credentials-governance-pack/blob/master/README.md#certification-status"><img alt="Certification: not certified" src="https://img.shields.io/static/v1?label=Certification&amp;message=not%20certified&amp;labelColor=1E293B&amp;color=92400E"></a>
<a href="https://github.com/groupsum/verifiable-credentials-governance-pack/blob/master/docs/governance/pack-authoring-guide.md"><img alt="Governance: pack governance" src="https://img.shields.io/static/v1?label=Governance&amp;message=pack%20governance&amp;labelColor=1E293B&amp;color=4338CA"></a>
<a href="https://github.com/groupsum/verifiable-credentials-governance-pack/actions/workflows/readme-standards.yml"><img alt="Evidence: README and wheel checks" src="https://img.shields.io/static/v1?label=Evidence&amp;message=README%20and%20wheel%20checks&amp;labelColor=1E293B&amp;color=6D28D9"></a>
</p>
<p align="center"><a href="#overview">Overview</a> · <a href="#installation">Installation</a> · <a href="#quick-start">Quick Start</a> · <a href="#usage">Usage</a> · <a href="#public-api-and-import-surfaces">API</a> · <a href="#contributing">Contributing</a> · <a href="#governance">Governance</a> · <a href="#license">License</a></p>
<!-- readme-standards:end branding -->

---

## Overview

### Summary

Installable SSOT governance pack for W3C Verifiable Credentials, presentations, securing mechanisms, status models, schema use, cryptosuite profiles, and adjacent issuance/presentation protocols.

### Why This Package

The pack supplies versioned, source-linked ADR and SPEC templates for Verifiable Credentials Governance.

### When to Use

Use this pack when a downstream SSOT Registry needs reusable decisions and requirements for Verifiable Credentials Governance.

### Features

**Included ADRs**

- [`adr:verifiable-credentials-are-attestable-claims-not-local-authentication-credentials`](https://github.com/groupsum/verifiable-credentials-governance-pack/blob/master/src/verifiable_credentials_governance_pack/templates/adr/ADR-1000-verifiable-credentials-are-attestable-claims-not-local-authentication-credentials.yaml) — Verifiable Credentials Are Attestable Claims Not Local Authentication Credentials
- [`adr:w3c-vc-data-model-is-the-core-credential-and-presentation-authority`](https://github.com/groupsum/verifiable-credentials-governance-pack/blob/master/src/verifiable_credentials_governance_pack/templates/adr/ADR-1001-w3c-vc-data-model-is-the-core-credential-and-presentation-authority.yaml) — W3C VC Data Model Is The Core Credential And Presentation Authority
- [`adr:vc-securing-mechanisms-are-profiled-as-data-integrity-and-jose-cose`](https://github.com/groupsum/verifiable-credentials-governance-pack/blob/master/src/verifiable_credentials_governance_pack/templates/adr/ADR-1002-vc-securing-mechanisms-are-profiled-as-data-integrity-and-jose-cose.yaml) — VC Securing Mechanisms Are Profiled As Data Integrity And JOSE COSE
- [`adr:vc-status-and-revocation-are-governed-through-explicit-status-mechanisms`](https://github.com/groupsum/verifiable-credentials-governance-pack/blob/master/src/verifiable_credentials_governance_pack/templates/adr/ADR-1003-vc-status-and-revocation-are-governed-through-explicit-status-mechanisms.yaml) — VC Status And Revocation Are Governed Through Explicit Status Mechanisms
- [`adr:dids-are-optional-identifiers-for-vc-not-a-vc-prerequisite`](https://github.com/groupsum/verifiable-credentials-governance-pack/blob/master/src/verifiable_credentials_governance_pack/templates/adr/ADR-1004-dids-are-optional-identifiers-for-vc-not-a-vc-prerequisite.yaml) — DIDs Are Optional Identifiers For VC Not A VC Prerequisite
- [`adr:openid4vc-protocols-are-transport-rails-not-vc-core`](https://github.com/groupsum/verifiable-credentials-governance-pack/blob/master/src/verifiable_credentials_governance_pack/templates/adr/ADR-1005-openid4vc-protocols-are-transport-rails-not-vc-core.yaml) — OpenID4VC Protocols Are Transport Rails Not VC Core
- [`adr:selective-disclosure-and-format-profiles-must-be-explicitly-declared`](https://github.com/groupsum/verifiable-credentials-governance-pack/blob/master/src/verifiable_credentials_governance_pack/templates/adr/ADR-1006-selective-disclosure-and-format-profiles-must-be-explicitly-declared.yaml) — Selective Disclosure And Format Profiles Must Be Explicitly Declared
- [`adr:vc-schemas-status-and-presentation-rules-are-owned-here`](https://github.com/groupsum/verifiable-credentials-governance-pack/blob/master/src/verifiable_credentials_governance_pack/templates/adr/ADR-1007-vc-schemas-status-and-presentation-rules-are-owned-here.yaml) — VC Schemas Status And Presentation Rules Are Owned Here

**Included SPECs**

- [`spc:verifiable-credential-data-model-contract`](https://github.com/groupsum/verifiable-credentials-governance-pack/blob/master/src/verifiable_credentials_governance_pack/templates/specs/SPEC-2000-verifiable-credential-data-model-contract.yaml) — Verifiable Credential Data Model Contract
- [`spc:verifiable-presentation-processing-contract`](https://github.com/groupsum/verifiable-credentials-governance-pack/blob/master/src/verifiable_credentials_governance_pack/templates/specs/SPEC-2001-verifiable-presentation-processing-contract.yaml) — Verifiable Presentation Processing Contract
- [`spc:vc-data-integrity-proof-contract`](https://github.com/groupsum/verifiable-credentials-governance-pack/blob/master/src/verifiable_credentials_governance_pack/templates/specs/SPEC-2002-vc-data-integrity-proof-contract.yaml) — VC Data Integrity Proof Contract
- [`spc:vc-jose-cose-securing-contract`](https://github.com/groupsum/verifiable-credentials-governance-pack/blob/master/src/verifiable_credentials_governance_pack/templates/specs/SPEC-2003-vc-jose-cose-securing-contract.yaml) — VC JOSE COSE Securing Contract
- [`spc:vc-status-and-revocation-contract`](https://github.com/groupsum/verifiable-credentials-governance-pack/blob/master/src/verifiable_credentials_governance_pack/templates/specs/SPEC-2004-vc-status-and-revocation-contract.yaml) — VC Status And Revocation Contract
- [`spc:vc-json-schema-and-vocabulary-contract`](https://github.com/groupsum/verifiable-credentials-governance-pack/blob/master/src/verifiable_credentials_governance_pack/templates/specs/SPEC-2005-vc-json-schema-and-vocabulary-contract.yaml) — VC JSON Schema And Vocabulary Contract
- [`spc:vc-cryptosuite-profile-contract`](https://github.com/groupsum/verifiable-credentials-governance-pack/blob/master/src/verifiable_credentials_governance_pack/templates/specs/SPEC-2006-vc-cryptosuite-profile-contract.yaml) — VC Cryptosuite Profile Contract
- [`spc:openid4vci-issuance-boundary-contract`](https://github.com/groupsum/verifiable-credentials-governance-pack/blob/master/src/verifiable_credentials_governance_pack/templates/specs/SPEC-2007-openid4vci-issuance-boundary-contract.yaml) — OpenID4VCI Issuance Boundary Contract
- [`spc:openid4vp-presentation-boundary-contract`](https://github.com/groupsum/verifiable-credentials-governance-pack/blob/master/src/verifiable_credentials_governance_pack/templates/specs/SPEC-2008-openid4vp-presentation-boundary-contract.yaml) — OpenID4VP Presentation Boundary Contract
- [`spc:dif-presentation-exchange-boundary-contract`](https://github.com/groupsum/verifiable-credentials-governance-pack/blob/master/src/verifiable_credentials_governance_pack/templates/specs/SPEC-2009-dif-presentation-exchange-boundary-contract.yaml) — DIF Presentation Exchange Boundary Contract
- [`spc:sd-jwt-vc-and-token-status-list-boundary-contract`](https://github.com/groupsum/verifiable-credentials-governance-pack/blob/master/src/verifiable_credentials_governance_pack/templates/specs/SPEC-2010-sd-jwt-vc-and-token-status-list-boundary-contract.yaml) — SD-JWT VC And Token Status List Boundary Contract

### Non-Goals

The pack supplies governance records. A downstream application implements the controls and collects its own conformance evidence.

---

## Getting Started

### Prerequisites

Use Python `>=3.10,<3.15`. Downstream synchronization also requires SSOT Registry and permission to write the target registry.

### Installation

#### uv

<!-- readme-standards:begin installation.uv -->
`verifiable-credentials-governance-pack` is not declared published. From the source checkout:

```bash
uv pip install .
```
<!-- readme-standards:end installation.uv -->

#### pip

<!-- readme-standards:begin installation.pip -->
`verifiable-credentials-governance-pack` is not declared published. From the source checkout:

```bash
python -m pip install .
```
<!-- readme-standards:end installation.pip -->

#### Poetry

<!-- readme-standards:begin installation.poetry -->
`verifiable-credentials-governance-pack` is not declared published. From a separate Poetry project, replace the path with your checkout:

```bash
poetry add /path/to/verifiable-credentials-governance-pack
```
<!-- readme-standards:end installation.poetry -->

### Quick Start

#### Example

<!-- readme-standards:begin example.quick-start -->
Source: [examples/quick_start.py](https://github.com/groupsum/verifiable-credentials-governance-pack/blob/master/examples/quick_start.py).

```python
"""Inspect the installed pack identity."""

from verifiable_credentials_governance_pack import load_pack_metadata

metadata = load_pack_metadata()
assert metadata["origin"]["id"] == "pack:verifiable-credentials-governance"
print(metadata["origin"]["id"])
```
<!-- readme-standards:end example.quick-start -->

#### Expected Result

The script prints `pack:verifiable-credentials-governance` from the installed pack metadata.

---

## Usage

### Common Workflows

<!-- readme-standards:begin example.usage -->
Source: [examples/usage.py](https://github.com/groupsum/verifiable-credentials-governance-pack/blob/master/examples/usage.py).

```python
"""Find a specification and its downstream path in the installed manifest."""

from verifiable_credentials_governance_pack import load_document_manifest

specification = next(
    row for row in load_document_manifest("spec")
    if row["id"] == "spc:verifiable-credential-data-model-contract"
)
assert specification["target_path"] == ".ssot/specs/SPEC-2000-verifiable-credential-data-model-contract.yaml"
```
<!-- readme-standards:end example.usage -->

Use the downstream environment that has both SSOT Registry and `verifiable-credentials-governance-pack` installed. Inspect the pack and preflight the target registry before approving synchronization.

```bash
uv run ssot pack inspect verifiable_credentials_governance_pack
uv run ssot pack preflight . verifiable_credentials_governance_pack --all
uv run ssot pack sync . verifiable_credentials_governance_pack --all --trust --yes
uv run ssot validate .
```

### Configuration

Select the installed import package `verifiable_credentials_governance_pack` in SSOT Registry. Review reservation owner `extension-pack:verifiable-credentials-governance-pack` and the target's trust policy before syncing.

### Error Handling

If preflight reports a schema, trust, or document-number conflict, resolve it in the target registry and repeat preflight before synchronization.

### Best Practices

Pin the pack version in downstream projects. Reference document IDs in local governance and inspect the change set before granting trust.

---

## Package Boundary

### What It Owns

Declared canonical VC ownership relative to customer profile integration.

### Public API and Import Surfaces

Import `load_pack_metadata`, `load_document_manifest`, and `read_packaged_document_text` from `verifiable_credentials_governance_pack` to inspect packaged records.

### Entry Points

<!-- readme-standards:begin entry-points -->
This package declares no command-line, GUI, or plugin entry points in its manifest.
<!-- readme-standards:end entry-points -->

### Injected Dependencies

The package binds its metadata and document loaders through `ssot-pack-contracts`. The caller supplies the target registry to SSOT Registry when synchronizing.

### Protocol Consumers

SSOT Registry uses the pack metadata, document manifests, and bundled templates during inspect, preflight, and sync.

### Extensions

Define downstream policies as local records and reference the pack's document IDs. Send proposed changes to the canonical pack through repository review.

---

## Operations and Readiness

### Operational Requirements

Local inspection reads installed package resources. Synchronization requires an initialized downstream registry and explicit operator approval.

### Health and Observability

Review the preflight and sync output, then use `ssot validate` to check the resulting registry.

### Security and Resource Limits

Implicit trust is disabled. Review the exact distribution, version, records, and reserved IDs before enabling trust in a target registry.

### Compatibility

- Python `>=3.10,<3.15`
- SSOT Registry schema `>=0.4.0`
- SSOT pack contracts `>=0.2.17,<0.3.0`

---

## Verification

### Tests

Run `python -m unittest discover -s tests -v` with the pack installed. The [README workflow](https://github.com/groupsum/verifiable-credentials-governance-pack/actions/workflows/readme-standards.yml) checks the source README and runs both examples against an installed wheel.

### Certification Status

The pack has no external certification. Downstream adoption requires evidence for the controls an application implements.

### Evidence

See the [README workflow](https://github.com/groupsum/verifiable-credentials-governance-pack/actions/workflows/readme-standards.yml) for package and documentation verification and the [packaged records](https://github.com/groupsum/verifiable-credentials-governance-pack/blob/master/src/verifiable_credentials_governance_pack/templates) for document-level sources.

---

## FAQ

### Why

**Why do document IDs matter?** Downstream records use them to trace an adopted decision or requirement to the pack that owns it.

### How

**How do I preview changes?** Use the registry's pack preflight before approving a sync.

### When

**When should I upgrade?** Read the changelog and preflight the new version against the target registry before applying it.

---

## Documentation and Related Packages

### More Documentation

See the [Pack guide](https://github.com/groupsum/verifiable-credentials-governance-pack/blob/master/docs/pack-guide.md), [changelog](https://github.com/groupsum/verifiable-credentials-governance-pack/blob/master/CHANGELOG.md), and [pack metadata](https://github.com/groupsum/verifiable-credentials-governance-pack/blob/master/src/verifiable_credentials_governance_pack/metadata.json).

### Related Packages

[SSOT Registry](https://pypi.org/project/ssot-registry/) manages downstream registries. [SSOT Pack Contracts](https://pypi.org/project/ssot-pack-contracts/) provides the shared pack interface.

### Project Links

<!-- readme-standards:begin project-links -->
- [Homepage](https://github.com/groupsum/verifiable-credentials-governance-pack)
- [Issues](https://github.com/groupsum/verifiable-credentials-governance-pack/issues)
- [Repository](https://github.com/groupsum/verifiable-credentials-governance-pack)
- [pypi: verifiable-credentials-governance-pack](https://pypi.org/project/verifiable-credentials-governance-pack/)
<!-- readme-standards:end project-links -->

---

## Contributing

### How to Contribute

Open an [issue](https://github.com/groupsum/verifiable-credentials-governance-pack/issues) or pull request describing the affected records, their authority, and the expected downstream effect.

### Development Setup

Install the checkout with `python -m pip install -e .`, then run `python -m unittest discover -s tests -v`. On Python 3.11 or newer, run `uvx --from readme-standards==0.1.3 readme-standards check`.

### Notes for Maintainers

Keep source links, document identifiers, and committed manifest hashes aligned. Run `uvx --from readme-standards==0.1.3 readme-standards render --write` after changing generated README inputs. Update the PyPI publication setting after the first successful upload.

---

## Governance

### Ownership and Decision Making

Groupsum maintains `pack:verifiable-credentials-governance`. The pack's reservation owner is `extension-pack:verifiable-credentials-governance-pack`. Downstream registry operators approve synchronization.

### Standards and Policies

**Authority Sources**

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

### Lifecycle and Migration

Review [release changes](https://github.com/groupsum/verifiable-credentials-governance-pack/blob/master/CHANGELOG.md) and preflight the chosen version against each downstream registry.

---

## License and Attribution

### License

<!-- readme-standards:begin license -->
Licensed under `Apache-2.0`. See [LICENSE](https://github.com/groupsum/verifiable-credentials-governance-pack/blob/master/LICENSE).
<!-- readme-standards:end license -->

### Notices

<!-- readme-standards:begin notices -->
No separate NOTICE file is declared. Review the license and bundled third-party attributions.
<!-- readme-standards:end notices -->
