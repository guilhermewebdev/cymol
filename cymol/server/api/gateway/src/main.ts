import express, { Express } from 'express';
import { MIDDLEWARES, PORT, HOST, SERVICES, INSTALLEDS_APPS, DEBUG } from './api/settings';
import { ApolloServer } from 'apollo-server-express';
import { ApolloGateway } from '@apollo/gateway';

const app:Express = express();
const gateway:ApolloGateway = new ApolloGateway({
    serviceList: SERVICES,
});
const server:ApolloServer = new ApolloServer({
    gateway,
    subscriptions: false,
    tracing: true,
    playground:DEBUG,
})
MIDDLEWARES.forEach((middleware:any) => app.use(middleware))
INSTALLEDS_APPS.forEach((subApp:Express) => app.use(subApp))
server.applyMiddleware({ app, path:'/', cors:true })
app.listen(PORT, HOST, () => console.log(`O servidor esta funcionando`))