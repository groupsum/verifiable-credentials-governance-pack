"""Find a specification and its downstream path in the installed manifest."""

from verifiable_credentials_governance_pack import load_document_manifest

specification = next(
    row for row in load_document_manifest("spec")
    if row["id"] == "spc:verifiable-credential-data-model-contract"
)
assert specification["target_path"] == ".ssot/specs/SPEC-2000-verifiable-credential-data-model-contract.yaml"
