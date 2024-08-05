const totalViewChart = document.getElementById('total-views-chart');
const revenueChart = document.getElementById('revenue-chart');
const growthRateChart = document.getElementById('growth-rate-chart');
const subscriberCountChart = document.getElementById('subscriber-count');
const trafficSourcesElement = document.getElementById('traffic-sources');
const datatable = document.getElementById('datatable');


fetch('/api/total-views')
.then (res => res.json())
.then (data =>{
    
    new Chart(totalViewChart, {
        type: 'line',
        data: {
            labels: data.labels,
            datasets: [{
                label: '# of Votes',
                data: data.data,
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    })
})



const estimatedRevenueChart = new Chart(revenueChart, {
    type: 'line',
    data: { 
        labels: ['Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Jan'],
    datasets: [{
        label: '# of Votes',
        data : [255, 280, 290, 179, 512, 580],
        borderWidth: 1
    }]
    }
 })
 
 new Chart(subscriberCountChart, {
    type: 'line',
    data: {
        labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
        datasets: [{
            label: '# of Votes',
            data: [12, 19 , 3, 5, 2, 3],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

const trafficSourcesChart = new Chart(trafficSourcesElement, {
    type: 'pie',
    data: {
        labels: ['Youtube', 'FaceBook', 'Snapchat', 'Google', 'FireFox', 'Opera'],
        datasets: [{
            label: '# share',
            data: [12, 19, 3, 5, 2, 3],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

// Initializing datatable
const dataTable = new simpleDatatables.DataTable("#datatable",  {
    searchable : true,
    fixeHeight: true,
    data: {
        headings: ["Video title", "Published Date", "Views Count"],
       

    }
})

fetch('/api/datatable-api')
.then (res => res.json())
.then (data =>{
    dataTable.rows.add(data.data)
})