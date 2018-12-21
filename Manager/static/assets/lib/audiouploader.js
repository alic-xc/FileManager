document.addEventListener('DOMContentLoaded',function(){
  document.querySelector('#button').onsubmit = function(){
    let audio =   document.querySelector("#audio").files
        if(audio[0][type] != "audio/wav" || audio[0][type] != "audio/mp3"){
          alert("Check Input. Failed Attempt")
          return false;
        }

      const request  = new xHttpRequest()
      request.open('POST','/train')
      request.onload = function(){

      }
      const data = new FormData()
      data.append(audio)
      request.send()




    console.log(audio);

    return false
  }
})

// function handleFile(file){
//     var file  = document.querySelector(`#${}`).files
// }
