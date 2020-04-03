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

export const csrfProtection = csrf({ cookie: true })

export const MIDDLEWARES:Array<any> = [
    helmet(),
    RateLimit({
        windowMs: 15*60*1000, // 15 minutes 
        max: 1000, // limit each IP to 100 requests per windowMs 
    }),
    hostValidation({ hosts: ALLOWED_HOSTS }),
    compression(),
    bodyParser.json({ type: 'application/*+json' }),
    cookieParser(),
    // csrfProtection,
];

export const MONGOOSE_CONF:any = {
    uri: 'mongodb://172.25.20.20:27017/api',
    options: {
        useNewUrlParser: true,
        useFindAndModify: false,
        useUnifiedTopology: true,
    },
}