"""Inspect the installed pack identity."""

from verifiable_credentials_governance_pack import load_pack_metadata

metadata = load_pack_metadata()
assert metadata["origin"]["id"] == "pack:verifiable-credentials-governance"
print(metadata["origin"]["id"])
