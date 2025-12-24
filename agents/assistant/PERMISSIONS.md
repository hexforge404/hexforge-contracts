# Assistant Permissions — Contract

Assistant may:
- create jobs (POST)
- poll jobs (GET)
- read public asset paths
- validate existence of files

Assistant may NOT:
- modify completed jobs
- delete public outputs
- write directly into `/assets/*` roots (unless explicitly permitted by a specific engine)
- access secrets outside its environment variables
