import mongoose from 'mongoose';
import { MongoError, MongoCallback } from 'mongodb';

export function connectDB(MONGOOSE_CONF:any){
    mongoose.connect(MONGOOSE_CONF.uri, MONGOOSE_CONF.opions)
    mongoose.connection.on('connected', (err:MongoError, res:any) => {
        console.log('Conectado com o banco de dados')
        mongoose.connection.on('disconnect', () => {
            console.log('Banco de dados desconectado')
            connectDB(MONGOOSE_CONF)            
        })
    })
    return mongoose.connection;
}