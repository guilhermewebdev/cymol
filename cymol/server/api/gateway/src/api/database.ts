import mongoose from 'mongoose';

export function connectDB(MONGOOSE_CONF:any){
    mongoose.connect(MONGOOSE_CONF.uri, MONGOOSE_CONF.opions)
    mongoose.connection.on('connected', () => {
        console.log('Conectado com o banco de dados')
        mongoose.connection.on('disconnect', () => {
            console.log('Banco de dados desconectado')
            connectDB(MONGOOSE_CONF)            
        })
    })
    return mongoose.connection;
}