/* All the javascript will be loaded after the html is finished loading.
* */
$(document).ready(() => {

    /* the print function is used to print the received data to the 
    * screen.
    * */
    function print(data, word) {
        console.log("hej");
        $("#result").html("");
        if (typeof data.success[word][0] == "string") {
            $("#result").append(`<b>${word}</b><br>`);
            $("#result").append("<ul>")
            data.success[word].forEach((e,i) => {
                $("#result").append(`
                    <li>${e}</li>
                `);
            });
            $("#result").append("</ul>")
        } else {
            data.success[word].forEach((definition,i) => {
                for (x in definition) {
                    $("#result").append(`<b>${x}</b><br>`);
                    $("#result").append("<ul>")
                    definition[x].forEach((e,i) => {
                        $("#result").append(`
                            <li>${e}</li>
                        `);
                    });
                    $("#result").append("</ul>")
                }
            });
        };
    };

    /* Here the actual html is written for the page
     * */
    $("#root").html(`
    <input id="field" class="bg-white mb-4 focus:outline-none focus:shadow-outline border border-gray-300 rounded-lg py-2 px-4 block w-full appearance-none leading-normal" type="text">
    <button id="search" class="bg-blue-500 mb-4 w-full hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">Button </button>
    <div id="result" class="mb-4 bg-gray"></div>
    `);

    /* If the search button is clicked then javascript will call our
     * Flask server and ask for the word searched in the input field
     * */
    $("#search").click(() => {
        var field = $("#field").val();
        $.ajax({
            url : `http://127.0.0.1:5000/${field}`,
            type: "GET",
            contentType: "application/json",
            success: function(data){
                print(data, field.toUpperCase())
            },
            error: function(data) {
                alert(data.responseJSON.error[field.toUpperCase()]);
            },
        });
    });
});
