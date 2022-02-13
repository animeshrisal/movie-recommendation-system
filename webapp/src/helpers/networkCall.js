function authHeader() {
    const user = localStorage.getItem('user')
    if (user) {
        return { 'Authorization': `JWT ${JSON.parse(user).access}` };
    } else {
        return {};
    }
}

const camelToSnakeCase = str => str.replace(/[A-Z]/g, letter => `_${letter.toLowerCase()}`);

export function authenticatedRequestGenerator(values= {}, method='POST') {

    const formData = new FormData();

    const requestOption = {
        method,
        headers: authHeader(),
    }

    if  (Object.keys(values).length !== 0){
        for ( var key in values ) {
            formData.append(camelToSnakeCase(key), values[key]);
        }
    }

    return {...requestOption, body: formData}
}

export function authenticatedGetRequestOption() {
    return {
        method: 'GET',
        headers: authHeader()
    }
}



