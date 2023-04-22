import subprocess


get_profiles = subprocess.run(['netsh', 'wlan', 'show', 'profiles'], stdout=subprocess.PIPE)
raw_profiles = get_profiles.stdout.decode('utf-8')


profiles =[]

for line in raw_profiles.split('\n'):
    if 'User Profile' in line:
        profile_prefix_space = line.split(':')[1]
        profile = profile_prefix_space[1:]
        #print(profile)
        profiles.append(profile)



for profile in profiles:
    profile_details = subprocess.run(['netsh', 'wlan', 'show', 'profile', profile[:-1], 'key=clear'], stdout=subprocess.PIPE)
    details = profile_details.stdout.decode('utf-8')
    for line in details.split('\n'):
        if 'Key Content' in line:
            pwd_with_space = line.split(':')[1]
            pwd = pwd_with_space[1:]
            print(profile)
            print_line = "    |================> " + pwd
            print(print_line)
            print()