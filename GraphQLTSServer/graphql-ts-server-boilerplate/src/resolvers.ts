import * as bcrypt from 'bcryptjs';
import { User } from './entity/User';

import { ResolverMap } from "./types/graphql-utils"

declare namespace GQL {
    interface IGraphQLResponseRoot {
    data?: IQuery | IMutation;
    errors?: Array<IGraphQLResponseError>;
    }
    
    interface IGraphQLResponseError {
    /** Required for all errors */
    message: string;
    locations?: Array<IGraphQLResponseErrorLocation>;
    /** 7.2.2 says 'GraphQL servers may provide additional entries to error' */
    [propName: string]: any;
    }
    
    interface IGraphQLResponseErrorLocation {
    line: number;
    column: number;
    }
    
    interface IQuery {
    __typename: "Query";
    hello: string;
    }
    
    interface IHelloOnQueryArguments {
    name?: string | null;
    }
    
    interface IMutation {
    __typename: "Mutation";
    register: boolean | null;
    }
    
    interface IRegisterOnMutationArguments {
    email: string;
    password: string;
    }
}


export const resolvers: ResolverMap = {
    Query: {
      hello: (_, { name }: GQL.IHelloOnQueryArguments) => `Bye ${name || 'World'}`,
    },

    Mutation: {
        register: async (_, { email, password }: GQL.IRegisterOnMutationArguments) => {
            const hashedPassword = await bcrypt.hash(password, 10);
            const user = User.create({
                email,
                password: hashedPassword
            });

            await user.save();
            return true;
        },
    }
}