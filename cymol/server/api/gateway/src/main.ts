import express, { Express } from 'express';
import { MIDDLEWARES, PORT, HOST, SERVICES, INSTALLEDS_APPS, DEBUG, MONGOOSE_CONF } from './api/settings';
import { ApolloServer } from 'apollo-server-express';
import { ApolloGateway, RemoteGraphQLDataSource } from '@apollo/gateway';
import { connectDB } from './api/database'
import { Connection } from 'mongoose';

const conn:Connection = connectDB(MONGOOSE_CONF)

const app:Express = express();

class AuthenticatedDataSource extends RemoteGraphQLDataSource {
    willSendRequest({ request, context }) {
      // Pass the user's id from the context to underlying services
      // as a header called `user-id`
      console.log(request)
      console.log(context)
      request.http.headers.set('user-id', context.userId);
    }
  }

const server:ApolloServer = new ApolloServer({
    gateway: new ApolloGateway({
        serviceList: SERVICES,
        buildService({ name, url }) {
            return new RemoteGraphQLDataSource({ url });
        },
        debug: DEBUG,
        __exposeQueryPlanExperimental: true,
    }),
    subscriptions: false,
    playground: DEBUG,
    engine: false,
    debug: DEBUG,
});

MIDDLEWARES.forEach((middleware:any) => app.use(middleware))
INSTALLEDS_APPS.forEach((subApp:Express) => app.use(subApp))
server.applyMiddleware({ app, path: '/', cors: true })
app.listen(PORT, HOST, () => console.log(`O servidor esta funcionando`))