# 3. Load the IFC file.
import ifcopenshell
ifc_file = ifcopenshell.open("AC20-FZK-Haus.ifc")
print("IFC file loaded:", ifc_file.schema)

# 4. Get and print the project name.
project = ifc_file.by_type("IfcProject")[0]
print("Project Name: ",project.Name)

# 5. Find all IfcStair elements and print the names and ids.
stairs = ifc_file.by_type("IFCStair")
print(f"Number of stairs: {len(stairs)}")
for stair in stairs:
	print(stair.GlobalId, stair.Name)

# 6. Find all IfcSlab elements and print the names and ids.
slabs = ifc_file.by_type("IFCSlab")
print(f"Number of slabs: {len(slabs)}")
for slab in slabs:
	print(slab.GlobalId, slab.Name)

# 7. Rename all slabs.
slabs = ifc_file.by_type("IfcSlab")
for i, slab in enumerate(slabs, 1):
    slab.Name = f"Renamed_Slab_{i}"
    print(f"Updated slab: {slab.GlobalId} → {slab.Name}")

# 8. Print the building storeys.
project = ifc_file.by_type("IfcProject")[0]

for site in project.IsDecomposedBy[0].RelatedObjects:
    for building in site.IsDecomposedBy[0].RelatedObjects:
        for storey in building.IsDecomposedBy[0].RelatedObjects:
            print("Storey", storey.Name, "Elevation", storey.Elevation)

# 9. List all object types in the file.
types = set(el.is_a() for el in ifc_file)
print("Object types in file:", types)

# 10. Save the updated IFC file.
ifc_file.write("AC20-FZK-Haus_renamed.ifc")
