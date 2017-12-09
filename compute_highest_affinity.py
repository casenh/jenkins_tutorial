
# No need to process files and manipulate strings - we will
# pass in lists (of equal length) that correspond to 
# sites views. The first list is the site visited, the second is
# the user who visited the site.

# See the test cases for more details.

def highest_affinity(site_list, user_list, time_list):
    # Returned string pair should be ordered by dictionary order
    # I.e., if the highest affinity pair is "foo" and "bar"
    # return ("bar", "foo"). 
    return("bar", "foo")

    # First generate the list of sites that each user visited.
    user_site_map = {}
    for i in range(0, len(site_list)):
        user = user_list[i]
        if user not in user_site_map:
            user_site_map[user] = []
        user_site_map[user].append(site_list[i])

    # Next, convert the list of sites for each user into all pairs of sites the
    # user visited. 
    user_site_pair_map = {}
    for user, site_list in user_site_map.items():
        user_site_pair_map[user] = []

        for i in range(0, len(site_list)):
            # We will have already compared the last element to all previous
            # elements in the list.
            if i == (len(site_list) - 1):
                break

            for n in range(i + 1, len(site_list)):
                # XXX: Make sure the sites are in alphabetical order so they
                # hash consistently.
                site_pair = sorted([site_list[i], site_list[n]])
                user_site_pair_map[user].append(':'.join(site_pair))

    # Lastly, determine which site pair has the highest affinity by counting
    # the number of times a pair of sites was visited for every pair.
    affinity_map = {}
    highest_affinity_count = 0
    highest_affinity_pair = None
    for user, site_pair_list in user_site_pair_map.items():
        for site_pair in site_pair_list:
            if site_pair not in affinity_map:
                affinity_map[site_pair] = 1
            else:
                affinity_map[site_pair] += 1

            if affinity_map[site_pair] > highest_affinity_count:
                highest_affinity_count = affinity_map[site_pair]
                highest_affinity_pair = site_pair

    result = highest_affinity_pair.split(':')
    return tuple(result)
