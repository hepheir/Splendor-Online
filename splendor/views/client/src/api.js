const HOST = 'http://localhost:5000';
const ASSET_INFO_CACHE = {};

async function api_get_asset_info(asset_type, asset_id) {
    const path = `/game_object/${asset_type}/${asset_id}`;
    if (path in ASSET_INFO_CACHE) {
        console.log('Cache hit!'); // DEBUG
        return ASSET_INFO_CACHE[path];
    }
    else {
        console.log('Cache miss!'); // DEBUG
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
        return ASSET_INFO_CACHE[path] = await response.json();
    }
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
