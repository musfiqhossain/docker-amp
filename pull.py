import sys, subprocess, json, requests

pr_commit_url = sys.argv[1]
# 'https://api.github.com/repos/musfiqhossain/docker-amp/pulls/21/commits'
response = requests.get(pr_commit_url)
json_data = json.loads(response.text)


print("arg ", sys.argv[1])

for c in json_data:
    sha =  c['sha']
    if c['commit']['message'].find("Merge") == -1:
            print("Checking commit ", c['commit']['message'])
            proc = subprocess.Popen(['git', 'branch','--contains' , sha, '|', 'grep', 'qa'], stdout=subprocess.PIPE)
            output = proc.stdout.read().decode('utf-8').strip()
            if output == 'qa':
                print('PR in QA')
            else:
                print('Cannot open PQ to main')
                sys.exit(1)
    else:
        print("skip merge", c['commit']['message'])
