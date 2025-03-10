"""
Resturant Table Seating System
Code2College assessment 2025
"""

from resturant_tables import restaurant_tables

def count_free_tables(tables: list, guests: int):
    
    #Level 1
    #returns the number of tables that are free and can seat the guests
    
    free_tables = 0
    for table in tables:
        if not table["occupied"] and table["capacity"] >= guests:
            free_tables += 1
    return free_tables

def find_free_tables(tables: list, party_size: int):
    
    #Level 2
    #returns the first table number that is free and can seat the guests

    for i, table in enumerate(tables):
        if not table["occupied"] and table["capacity"] >= party_size:
            return table["table_id"]
    return None

def show_all_tables_that_can_seat(tables: list, guests: int):
   
    #Level 3
    #returns the multiple table numbers the guests can sit in
    
    free_tables = []
    for table in tables:
        if not table["occupied"] and table["capacity"] >= guests:
            free_tables.append(table["table_id"])
    return free_tables
    
def find_tables_with_combos(tables: list, party_size: int):
    
    #Level 4
    #returns the table numbers that can seat the guests in a combination of tables
    
    results = []

    for table in tables:
        if not table["occupied"]:
            combo_capacity = table["capacity"]
            combo_tables = [table["table_id"]]
            for neighbor_id in table.get("neighbors", []):
                neighbor_table = next((t for t in tables if t["table_id"] == neighbor_id), None)
                if neighbor_table and not neighbor_table["occupied"]:
                    combo_capacity += neighbor_table["capacity"]
                    combo_tables.append(neighbor_table["table_id"])
                    if combo_capacity >= party_size:
                        combo = tuple(sorted(combo_tables))
                        if combo not in results:
                            results.append(combo)
                        break  # Stop checking more neighbors once a valid combo is found       
    return results

def print_friendly_output(tables: list, party_size: int):
    
    #prints friendly output for the table combinations

    combos = find_tables_with_combos(tables, party_size)
    output = []
    for combo in combos:
        if len(combo) == 1:
            table_id = combo[0]
            table = next(t for t in tables if t["table_id"] == table_id)
            output.append(f"Table {table_id} is free and can seat {table['capacity']} people.")
        else:
            total_capacity = sum(next(t["capacity"] for t in tables if t["table_id"] == table_id) for table_id in combo)
            combo_str = " and ".join(f"Table {table_id}" for table_id in combo)
            output.append(f"{combo_str} together can seat {total_capacity} people.")
    return "\n".join(output)

def main():
    header = restaurant_tables[0]
    tables = []
    for i in range(1, len(header)):
        table_id = int(header[i][1])
        capacity = int(header[i][3])
        neighbors = []
        if i > 1:
            neighbors.append(int(header[i-1][1]))
        if i < len(header) - 1:
            neighbors.append(int(header[i+1][1]))
        for j in range(1, len(restaurant_tables)):
            if restaurant_tables[j][i] == 'o':
                occupied = False
            else:
                occupied = True
            tables.append({"table_id": table_id, "capacity": capacity, "occupied": occupied, "neighbors": neighbors})

    party_size = 6
    print("Level 1: " + str(count_free_tables(tables, party_size)))
    print("Level 2: " + str(find_free_tables(tables, party_size)))
    print("Level 3: " + str(show_all_tables_that_can_seat(tables, party_size)))
    print("Level 4: " + str(find_tables_with_combos(tables, party_size)))
    print("Bonus: \n" + print_friendly_output(tables, party_size))

if __name__ == "__main__":
    main()  #run the function