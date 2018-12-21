document.addEventListener('DOMContentLoaded',function(){
  document.querySelector('#audio').onclick = function(){

        const link = 'http://127.0.0.1:5000/play/'
        this.querySelector('i').className = "fa fa-pause"
        let audio  = document.createElement('audio')
        audio.style.display = "none"
        audio.src = `${link+this.dataset.link}`
        audio.autoplay = true
        audio.onended = ()=>{
          this.querySelector('i').className = "fa fa-play"
          audio.remove()
        }
        document.body.append(audio);
      }

  document.querySelectorAll('#extra-link').forEach(function(a){
    a.onclick = function(){
        dataRequest(a.dataset.link)
    }
  })

  document.querySelectorAll('#record-audio').forEach(function(file){
    file.onclick  = function(){
          const link = 'http://127.0.0.1:5000/play_convert/'
          let path = this.dataset.path.trim()
          let name = this.dataset.name.trim()
          this.querySelector('i').className = "fa fa-pause"
          let audio  = document.createElement('audio')
          audio.style.display = "none"
          audio.src = `${link+path}/${name}`
          audio.autoplay = true
          audio.onended = ()=>{
            this.querySelector('i').className = "fa fa-play"
            audio.remove()
          }
          document.body.append(audio);
        }
  })

})
function dataRequest(id){
  let xhr = new XMLHttpRequest()
  xhr.open('POST','/advert',true)
  xhr.onload = function() {
    const response = JSON.parse(xhr.responseText)
    if(response.status == 'ok'){
      document.querySelector('#request-name').innerHTML = response.data.name
      document.querySelector('#request-length').innerHTML = response.data.length
      document.querySelector('#request-start').innerHTML = response.data.timefrom
      document.querySelector('#request-stop').innerHTML = response.data.timeto
      document.querySelector('#audio').dataset.link = response.data.file

    }else{
      document.querySelector('#request-name').innerHTML = "None"
      document.querySelector('#request-length').innerHTML = "None"
      document.querySelector('#request-start').innerHTML = "None"
      document.querySelector('#request-stop').innerHTML = "None"
      document.querySelector('#audio').dataset.link = "None"
    }
  }
  const form = new FormData()
  form.append('id',id)
  xhr.send(form)
}
