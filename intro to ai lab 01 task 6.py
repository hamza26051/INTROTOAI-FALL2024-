dict={
    "Physics":40,
    "Chemistry":78,
    "Math":82
}
values=dict.values()
marks= sum(values)

average=marks/len(values)
highest=max(values)

print(average)
print(highest)