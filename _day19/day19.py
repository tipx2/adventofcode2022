from parse import parse
import random
with open("input19.txt") as f:
    lines = f.readlines()

# each line be like: [id, rb_ore_cost, rb_clay_cost, rb_obby_ore_cost, rb_obby_clay_cost, rb_geode_ore_cost, rb_geode_obby_cost]
for x in range(len(lines)):
    lines[x] = parse("Blueprint {}: Each ore robot costs {} ore. Each clay robot costs {} ore. Each obsidian robot costs {} ore and {} clay. Each geode robot costs {} ore and {} obsidian.", lines[x].strip())

print(lines)
class run:
    def __init__(self, line):
        self.ore = 0
        self.clay = 0
        self.obby = 0
        self.geode = 0
        
        self.ore_bots = 1
        self.clay_bots = 0
        self.obby_bots = 0
        self.geode_bots = 0
        
        self.id = int(line[0])
        self.rb_ore_cost = int(line[1])
        self.rb_clay_cost = int(line[2])
        self.rb_obby_ore_cost = int(line[3])
        self.rb_obby_clay_cost = int(line[4])
        self.rb_geode_ore_cost = int(line[5])
        self.rb_geode_obby_cost = int(line[6])
        
    
    def check_what_to_buy(self):
        options = [""]
        if self.ore >= self.rb_ore_cost:
            options.append("ore_bot")
        if self.ore >= self.rb_clay_cost:
            options.append("clay_bot")
        if self.ore >= self.rb_obby_ore_cost and self.clay >= self.rb_obby_clay_cost:
            options.append("obby_bot")
            options.append("obby_bot")
            options.append("obby_bot")
            options.append("obby_bot")
            options.append("obby_bot")
            options.append("obby_bot")
            options.append("obby_bot")
            options.append("obby_bot")
            options.append("obby_bot")
            options.append("obby_bot")
            options.append("obby_bot")
            options.append("obby_bot")
        if self.ore >= self.rb_geode_ore_cost and self.obby >= self.rb_geode_obby_cost:
            options.append("geode_bot")
            options.append("geode_bot")
            options.append("geode_bot")
            options.append("geode_bot")
            options.append("geode_bot")
            options.append("geode_bot")
            options.append("geode_bot")
            options.append("geode_bot")
            options.append("geode_bot")
            options.append("geode_bot")
            options.append("geode_bot")
            options.append("geode_bot")
            options.append("geode_bot")
            options.append("geode_bot")
            options.append("geode_bot")
            options.append("geode_bot")
            options.append("geode_bot")
            options.append("geode_bot")
            options.append("geode_bot")
            options.append("geode_bot")
            options.append("geode_bot")
            options.append("geode_bot")
            options.append("geode_bot")
            options.append("geode_bot")
            options.append("geode_bot")
            options.append("geode_bot")
            options.append("geode_bot")
            options.append("geode_bot")
            options.append("geode_bot")
            options.append("geode_bot")
            options.append("geode_bot")
            options.append("geode_bot")
        return options
    
    def buy_bot(self, bot):
        if bot == "ore_bot":
            self.ore -= self.rb_ore_cost
        elif bot == "clay_bot":
            self.ore -= self.rb_clay_cost
        elif bot == "obby_bot":
            self.ore -= self.rb_obby_ore_cost
            self.clay -= self.rb_obby_clay_cost
        elif bot == "geode_bot":
            self.ore -= self.rb_geode_ore_cost
            self.obby -= self.rb_geode_obby_cost
            
    def collect_minerals(self):
        self.ore += self.ore_bots
        self.clay += self.clay_bots
        self.obby += self.obby_bots
        self.geode += self.geode_bots
    
    def get_bot(self, bot):
        if bot == "ore_bot":
            self.ore_bots += 1
        elif bot == "clay_bot":
            self.clay_bots += 1
        elif bot == "obby_bot":
            self.obby_bots += 1
        elif bot == "geode_bot":
            self.geode_bots += 1
        
quality_levels = []

# part 2
lines = lines[0:3]

part2_maxes = [29, 4, 17]

for g in range(len(lines)):
    max_geodes = part2_maxes[g]
    for k in range(50_000_000):
        if k % 10_000_000 == 0:
            print("aryehvalue", k, g+1)
        a = run(lines[g])
        for _ in range(32):
            buys = a.check_what_to_buy()
            if buys != []: # if we can afford something
                choice = random.choice(buys)
                a.buy_bot(choice)
                a.collect_minerals()
                a.get_bot(choice)
            else:
                a.collect_minerals()
    
        if a.geode > max_geodes:
            max_geodes = a.geode
    # we assume we have the largest number of geodes
    part2_maxes[g] = max_geodes

print(part2_maxes)
print(part2_maxes[0] * part2_maxes[1] * part2_maxes[2])

# buying phase
# collecting phase
# new robot creation phase

# part 1 final array (after loads of iteration) quality_levels = [2, 0, 0, 0, 50, 24, 49, 0, 0, 40, 0, 0, 104, 98, 15, 32, 17, 18, 19, 40, 42, 44, 115, 0, 0, 0, 54, 168, 29, 0]