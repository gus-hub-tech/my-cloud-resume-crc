// Replace 'gustav-kiewiets-resume' with a unique key for your site
fetch('https://5k7cocswwa.execute-api.af-south-1.amazonaws.com/visitorcount/my-cloud-resume-crc-lambda-function')
    .then(res => res.json())
    .then(data => {
        // If using Lambda Proxy, parse the body
        const body = typeof data.body === "string" ? JSON.parse(data.body) : data;
        document.getElementById('visitorcount').textContent = body.visitor_count;
    })
    .catch(() => {
        document.getElementById('visitorcount').textContent = 'Unavailable';
    });