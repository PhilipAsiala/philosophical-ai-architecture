package moepa.praxeology

import rego.v1

# Physics of action: possible or impossible. Not a permission.
default allow_action := false

allow_action if {
	input.action == "record_income"
	input.flags.evidence_present == true
	input.resources.review_slots >= 1
	input.satisfiable.ledger_appended == true
}

allow_action if {
	input.action == "export_pii"
	input.flags.vendor_request == true
	input.resources.review_slots >= 1
	input.satisfiable.ledger_appended == true
}

allow_action if {
	input.requested_state == "transition_to_production"
	input.current_state == "staged"
}
