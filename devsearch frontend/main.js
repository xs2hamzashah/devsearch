let loginBtn = document.getElementById('login-btn');
let logoutBtn = document.getElementById('logout-btn');


let token = localStorage.getItem('token');

if(token){
    loginBtn.remove();
}else {
    logoutBtn.remove();
}

logoutBtn.addEventListener('click', (e)=> {
    e.preventDefault();
    localStorage.removeItem('token');
    window.location = 'http://127.0.0.1:5500/login.html'
})

let projectUrl = 'http://127.0.0.1:8000/api/projects/'

let getProjects = () => {
    
    fetch(projectUrl)
    .then(response => response.json())
    .then(data => {
        console.log(data);
        buildProjects(data)
    })

};


let buildProjects = (projects) => {
    let projectwrapper = document.getElementById("projects--wrapper");
     projectwrapper.innerHTML = ''
   
    for (let i = 0; i < projects.length; i++) {
        let project = projects[i];
        
        let projectCard = `
                <div class="project--card">
                    <img src="http://127.0.01:8000${project.featured_image}"
                    <div>
                        <div class="card--header">
                            <h3>${project.title}</h3>
                            <strong class="vote--option" data-vote="up" data-project="${project.id}">&#43;</strong>
                            <strong class="vote--option" data-vote="down" data-project="${project.id}">&#8722;</strong>
                        </div>  
                        <i>${project.vote_ratio}% Positive feedback</i>  
                        <p>${project.description.substring(0,150)}</p>
                    </div>
                </div>
        `
        projectwrapper.innerHTML += projectCard
    }
    // Add an event listener
    addVoteEvents();

}   

let addVoteEvents = ()=> {
    let voteBtns = document.getElementsByClassName("vote--option");
    
    for(let i=0; voteBtns.length > i; i++){
        voteBtns[i].addEventListener('click', (e)=> {
            // let token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjU0MjY0OTk2LCJpYXQiOjE2NTQxNzg1OTYsImp0aSI6IjRlNzIzYTE2NWNkODQzNmZhMDJlMDhiY2VkNjUzZDBmIiwidXNlcl9pZCI6Mn0.T4l73nyDGskuwu6sVpuljAYAJZoM5UavFwIciPRyics'
            let token = localStorage.getItem('token')

            let vote = e.target.dataset.vote;
            let project = e.target.dataset.project;
            
            fetch(`${projectUrl}${project}/vote/`, {
                method:'POST', 
                headers: {
                    'Content-Type': 'application/json',
                    Authorization: `Bearer ${token}`
                }, 
                body:JSON.stringify({'value': vote})
            })
            .then(response => response.json())
            .then(data =>{
                 console.log('Success', data);
                 getProjects();
                })

        })
    }
}

getProjects();