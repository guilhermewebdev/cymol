import express, { Express } from 'express';
import { MIDDLEWARES, PORT, HOST, SERVICES, INSTALLEDS_APPS, DEBUG, MONGOOSE_CONF } from './api/settings';
import { ApolloServer } from 'apollo-server-express';
import { ApolloGateway, RemoteGraphQLDataSource } from '@apollo/gateway';
import { connectDB } from './api/database'
import { Connection } from 'mongoose';

const conn:Connection = connectDB(MONGOOSE_CONF)

const app:Express = express();

const server:ApolloServer = new ApolloServer({
    gateway: new ApolloGateway({
        serviceList: SERVICES,
        debug: DEBUG,
        __exposeQueryPlanExperimental: true,
        introspectionHeaders: {
            Authorization: 'my-header'
        },
        buildService({ url }){
            return new RemoteGraphQLDataSource({ 
                url,
                willSendRequest: ({ request, context }) => {
                    console.log(context)
                    request.http.headers.set('authorization', context.authScope);
                }
            });
        }
    }),
    subscriptions: false,
    playground: DEBUG,
    engine: false,
    debug: DEBUG,
    context: (integrationContext) => ({
        authScope: integrationContext.req.headers.authorization
    })
});

MIDDLEWARES.forEach((middleware:any) => app.use(middleware))
INSTALLEDS_APPS.forEach((subApp:Express) => app.use(subApp))
server.applyMiddleware({ app, path:'/api/', cors: true })
app.listen(PORT, HOST, () => console.log(`O servidor esta funcionando`))