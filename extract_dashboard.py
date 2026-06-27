import json

log_file = "/home/caio/.gemini/antigravity/brain/2c6f3e04-fbf6-4263-939a-0615a375f139/.system_generated/logs/transcript_full.jsonl"

found = False
with open(log_file, "r") as f:
    for line in f:
        try:
            data = json.loads(line)
            if data.get("type") == "PLANNER_RESPONSE":
                for call in data.get("tool_calls", []):
                    if call.get("name") == "write_to_file":
                        args = call.get("args", {})
                        if args.get("TargetFile", "").endswith("dashboard.html"):
                            if "v-if=\"pg2==='execs'\"" not in args.get("CodeContent", ""):
                                # Found the good one, not the truncated one
                                print(args.get("CodeContent"))
                                found = True
                                break
        except Exception:
            pass
        if found: break
