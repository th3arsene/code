wo = "*"
for i in range(8):
    print(wo.center(40))
    wo = str.join(wo, "**")
wo = wo[:-2]
for i in range(8):
    wo = wo[:-2]
    print(wo.center(40))
