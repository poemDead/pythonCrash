def make_album(singer,title,num=None):
    album = {
        'singer':singer.title(),
        'title':title.title(),
    }
    if num:
        album['number_of_songs'] = num
    return album

wubai = make_album('wubai','aiqingdejintou')
print(wubai)
jielun = make_album('jay','qilixiang')
print(jielun)
begin = make_album('various artists','begin again',12)
print(begin)