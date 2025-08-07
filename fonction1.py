def display_progress(total_files) :
  for i in range(total_files) :
    print(f"downloading file {i} out of {total_files}")

n = input("nombre de fichiers svp: ")

display_progress(int(n))
print()
input("Press any key to continue …")
#time.sleep(3)