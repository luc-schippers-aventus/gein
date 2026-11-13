const BASEURL = "https://pokeapi.co/api/v2/";
const div = document.getElementById("pokemon")
async function pokeData(request){
    const response = await fetch(BASEURL + request);

    if (!response.ok)
    {
        console.log("Error getting pokedata. Error: " + response.status)
        return;
    }

    const data = await response.json()

    return data
}

async function searchPokemon(i)
{
    div.innerHTML = ''
    const data = await pokeData("pokemon/" + i)

    const content = document.createElement("p")
    content.style = "font-size: 30px"
    content.innerHTML = `
    <ul>
        <li>Name: ${data.name}</li>
        <li> Height: ${data.height}</li>
    </ul>
    `

    div.appendChild(content)

    console.log(data.name)
}

async function getPokemon()
{
    const data = await pokeData("pokemon?limit=10000")

    data.results.forEach((pokemon, i) => {
        const text = document.createElement("h3")
        text.textContent = `${i + 1}: ${pokemon.name}`

        const button = document.createElement("button")
        button.type = "button"
        button.textContent = pokemon.name
        button.addEventListener('click', () => {
            searchPokemon(i + 1)
        })

        div.appendChild(text)
        div.appendChild(button)
    });

}

getPokemon()