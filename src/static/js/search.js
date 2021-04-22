const searchInput = document.querySelector('#search-input')
const loadTableSearch = document.querySelector('.load-table-search')
const loadTableData = document.querySelector('.load-table-data')
const paginationData = document.querySelector('.pagination-data')

loadTableSearch.style.display = 'none'

searchInput.addEventListener('keyup', (e) => {
    let query = e.target.value;

    if (query.length > 0) {

        loadTableSearch.innerHTML = ""

        fetch('/expense/search', {
            method: 'POST',
            body: JSON.stringify({searchText: query})
        }).then((resp) => resp.json())
            .then((data) => {

                loadTableSearch.style.display = 'contents'
                loadTableData.style.display = 'none'
                paginationData.style.display = 'none'

                if (data.length === 0) {
                    loadTableSearch.innerHTML = "No result found"
                } else {
                    let index = 0;
                    data.forEach(item => {
                        loadTableSearch.innerHTML += `
                            <tr>
                            <td>${index += 1}</td>
                            <td>${item.amount}</td>
                            <td>${item.category}</td>
                            <td>${item.description}</td>
                            <td>${item.date}</td>
                            <td>
                            <a href="update/expense/${item.id}" class="btn btn-primary btn-sm">Edit</a>
                            <a href="delete/expense/${item.id}" class="btn btn-danger btn-sm">Delete</a>
                            </td>
                            </tr>
                        `
                    })
                }
            })
    } else {
        loadTableSearch.style.display = 'none'
        loadTableData.style.display = 'contents'
        paginationData.style.display = 'block'
    }
})
