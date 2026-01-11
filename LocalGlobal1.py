No = 11        # Global  (data defination statement)

def Fun():
    No = 21    # Local         (data defination statement)
    print("Value of No from fun is :", No)   # 21

print("Value of No is :", No)                # 11
Fun()