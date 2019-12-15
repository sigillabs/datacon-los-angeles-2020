import sys

def sieve_of_eratosthenes(ceiling):
  """
  Fill in this function.

  Return a list of prime numbers up to and including ceiling.

  See https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes for a definition of the sieve.
  """

  results = list(range(2, ceiling+1))
  top = results[-1]

  for i in results:
    if i > top:
      break

    j = 2
    while j*i <= top:
      if j*i in results:
        results.remove(j*i)
      j+=1

  return results

def main():
  if len(sys.argv) < 2:
    print("Please pass a ceiling to the sieve.")
    sys.exit(1)

  try:
    ceiling = int(sys.argv[1])
  except ValueError:
    print("Please pass a positive integer to the sieve.")
    sys.exit(1)

  if ceiling < 0:
    print("Please pass a positive integer to the sieve.")
    sys.exit(1)
  
  print(sieve_of_eratosthenes(ceiling))

main()