"use-strict";

import "../lib/socket.io.js";


const hostname = 'localhost:5000';
const port = 5000;
const namespace = '/lobby';

const socket = io(`ws://${hostname}:${port}${namespace}`);
