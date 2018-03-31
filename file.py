import os
import sys
import zipfile
import argparse
directory = os.path.dirname(os.path.abspath(__file__))

class MyClass:
    def fact(self,x):
        result = lambda n:reduce(lambda x,n:[x[1],x[0]+x[1]], range(n),[0,1])[0]
        return result(x)
    
    def unzip(self, path_to_zip_file, directory_to_extract_to):
        print path_to_zip_file
        zip_ref = zipfile.ZipFile(path_to_zip_file, 'r')
        zip_ref.extractall(directory_to_extract_to)
        zip_ref.close()


    def absoluteFilePaths(self,directory):
        for dirpath, _, filenames in os.walk(directory):
            # print filenames
            # print dirpath
            for f in filenames:
                # print os.path.abspath(os.path.join(dirpath, f)), dirpath
                if f.endswith('zip'):
                    print f
                    unzip(os.path.abspath(os.path.join(dirpath, f)), dirpath)
                # unzip()
                # yield os.path.abspath(os.path.join(dirpath, f))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("fact", type=int,
                        help="display a fact of a given number")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="increase output verbosity")
    args = parser.parse_args()

    myobject = MyClass()
    answer = myobject.fact(args.fact)
    if args.verbose:
        print "the factorial of {} equals {}".format(args.fact, answer)
    else:
        print answer

if __name__ == "__main__":
    main()