function modalOpen(e){
    console.log(e)

    var modal = document.getElementById("modal")
    var form = document.getElementById("form")
    modal.style.display = "block";
    document.getElementsByTagName("html")[0].style.overflow = "hidden";
    // modal.appendChild("<input type='null' name='modal' value=`${e}`>")
    var input = document.createElement('input')
    input.setAttribute("value", e)
    input.setAttribute("type", 'null')
    input.setAttribute("name", 'modal')
    input.setAttribute("id", 'nullModalInput')
    input.style.display = "none";
    input.innerHTML = e
    form.appendChild(input)
}

function modalClose(){
    modal.style.display = "none";
}

window.onclick = function(event) {
    if (event.target == modal) {
      modal.style.display = "none";
    }
  }


function contextModal(e){

  // window.location.href = "./footballmanager"

  var modal = document.getElementById("modal")
  modal.style.display = "block";

  console.log(e)
}

var currentPage = "offense"

function showOffense(){
  var offense = document.getElementById("offense")
  var defense = document.getElementById("defense")

  if(currentPage != "offense"){
    offense.style.display = "block"
    defense.style.display = "none"
    currentPage="offense"
  }
}

function showDefense(){
  var defense = document.getElementById("defense")
  var offense = document.getElementById("offense")

  if(currentPage != "defense"){
    defense.style.display = "block"
    offense.style.display = "none"
    currentPage="defense"
  }
}




















new autoComplete({
    data: {                              // Data src [Array, Function, Async] | (REQUIRED)
      src: async () => {
        // API key token
        // User search query
        const query = document.querySelector("#autoComplete").value;
        // Fetch External Data Source
        const source = await fetch('./names');
        // Format data into JSON
        const data = await source.json();
        // Return Fetched data
        return data.recipes;
      },
      key: ["title"],
      cache: false
    },
    query: {                             // Query Interceptor               | (Optional)
          manipulate: (query) => {
            return query.replace("pizza", "burger");
          }
    },
    sort: (a, b) => {                    // Sort rendered results ascendingly | (Optional)
        if (a.match < b.match) return -1;
        if (a.match > b.match) return 1;
        return 0;
    },
    placeHolder: "Player Names...",     // Place Holder text                 | (Optional)
    selector: "#autoComplete",           // Input field selector              | (Optional)
    observer: true,                      // Input field observer | (Optional)
    threshold: 3,                        // Min. Chars length to start Engine | (Optional)
    debounce: 300,                       // Post duration for engine to start | (Optional)
    searchEngine: "strict",              // Search Engine type/mode           | (Optional)
    resultsList: {                       // Rendered results list object      | (Optional)
        container: source => {
            source.setAttribute("id", "food_list");
        },
        destination: "#autoComplete",
        position: "afterend",
        element: "ul"
    },
    maxResults: 5,                         // Max. number of rendered results | (Optional)
    highlight: {
        render: true,                    // Highlight matching results        | (Optional)
    },
    resultItem: {                          // Rendered result item            | (Optional)
        content: (data, source) => {
            source.innerHTML = data.match;
        },
        element: "li"
    },
    noResults: (dataFeedback, generateList) => {
        // Generate autoComplete List
        generateList(autoCompleteJS, dataFeedback, dataFeedback.results);
        // No Results List Item
        const result = document.createElement("li");
        result.setAttribute("class", "no_result");
        result.setAttribute("tabindex", "1");
        result.innerHTML = `<span style="display: flex; align-items: center; font-weight: 100; color: rgba(0,0,0,.2);">Found No Results for "${dataFeedback.query}"</span>`;
        document.querySelector(`#${autoCompleteJS.resultsList.idName}`).appendChild(result);
    },
    onSelection: feedback => {             // Action script onSelection event | (Optional)
        console.log(feedback.selection.value.image_url);
    }
});