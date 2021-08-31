const HOST = 'http://172.20.10.6:5000';


async function api_get_asset_info(asset_type, asset_id) {
    const path = `/game_object/${asset_type}/${asset_id}`;
    const response = await fetch(
        HOST + path,
        {
            method: 'GET',
            mode: 'cors',
            cache: 'no-cache',
            headers: {
                'Content-Type': 'text/plain',
            },
        }
    )
    return await response.json();
}

async function api_get_game_status_card_supplier(card_level) {
    const path = `/game_status/card_supplier/${card_level}`;
    const response = await fetch(
        HOST + path,
        {
            method: 'GET',
            mode: 'cors',
            cache: 'no-cache',
            headers: {
                'Content-Type': 'text/plain',
            },
        }
    )
    return await response.json();
}


export {
    HOST,
    api_get_asset_info,
    api_get_game_status_card_supplier,
};
