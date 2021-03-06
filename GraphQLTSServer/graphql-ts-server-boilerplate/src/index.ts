import "reflect-metadata";

import * as path from 'path';

import { GraphQLServer } from 'graphql-yoga'
import { importSchema } from 'graphql-import'
import { resolvers } from "./resolvers";
import { createConnection } from "typeorm";



export const startServer = async () => {
    const typeDefs = importSchema(path.join(__dirname, './schema.graphql')); // or .gql or glob pattern like **/*.graphqls

    const server = new GraphQLServer({ typeDefs, resolvers })

    await createConnection();
    await server.start();
    console.log('Server is running on localhost:4000');
}

startServer();