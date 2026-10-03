package moepa.axiology

import rego.v1

# Ethics and compliance. Runs after praxeology. A possible act can still be denied.
default deny_action := false

deny_action if {
	input.commit_eligible == false
}

deny_action if {
	input.action == "export_pii"
}

deny_action if {
	input.requested_state == "transition_to_production"
	input.user_clearance < input.required_clearance
}
