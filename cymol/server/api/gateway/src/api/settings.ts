import helmet from 'helmet';
import compression from 'compression';
import csrf from 'csurf';
import cookieParser from 'cookie-parser';
import cors from 'cors';
import hostValidation from 'host-validation';
import RateLimit from 'express-rate-limit';
import { Express } from 'express';
import bodyParser from 'body-parser';
import { ServiceDefinition } from '@apollo/federation/src/composition/types';

export const DEBUG:boolean = true;

export const PORT:number = 4000;

export const HOST:string = '::';

export const ALLOWED_HOSTS:Array<string> = ['localhost'];

export const INSTALLEDS_APPS:Array<Express> = [];

export const SERVICES:Array<any> = [
    { name: 'auth', url: 'http://172.35.10.20:8000/graphql' },
];

export const MIDDLEWARES:Array<any> = [
    helmet(),
    // cookieParser(),
    bodyParser(),
    cors(),
    compression(),
    // csrf({cookie:true}),
    hostValidation({ hosts:ALLOWED_HOSTS }),
    // RateLimit({
    //     windowMs: 15*60*1000, // 15 minutes 
    //     max: 100, // limit each IP to 100 requests per windowMs 
    // }),
];

export const MONGOOSE_CONF:any = {
    uri: 'mongodb://172.25.20.20:27017/api',
    options: {
        useNewUrlParser: true,
        useFindAndModify: false,
        useUnifiedTopology: true,
    },
}