import React, { useState } from 'react';

function StudentRegister() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [email, setEmail] = useState('');

    const handleSubmit = (event: React.FormEvent) => {
        event.preventDefault();
        // Aquí puedes manejar la lógica de registro
        // Por ejemplo, puedes hacer una solicitud HTTP a tu servidor
    }

    return (
        <main className="h-screen flex flex-col items-center justify-center">
            <h2 className="text-4xl mb-4 md:mb-6 font-bold hover:drop-shadow-[0_0_0.3rem_#ffffff70] text-gray-200 hover:duration-300 text-center duration-400">Student Register</h2>
            <div className='bg-gradient-to-b from-black from-75% to-violet-900 hover:duration-200 grid justify-items-center rounded-3xl py-6 md:py-5 shadow-md shadow-purple-600 border-[1px] hover:shadow-violet-500 hover:shadow-lg border-purple-950 w-full max-w-screen-lg mx-auto'>
                <form onSubmit={handleSubmit} className="space-y-4 md:space-y-3 p-4 md:p-6 w-full mx-auto">
                    <div className="text-sm mb-2">
                        <label>
                            Student name:
                            <input type="text" value={username} onChange={e => setUsername(e.target.value)} className="block w-full mt-4 hover:drop-shadow-[0_0_0.1rem_#ffffff70] duration-400 p-2 md:p-1 text-center text-gray-300 md:text-[15px] hover:text-white border border-purple-400 shadow shadow-purple-950 hover:duration-300 hover:shadow-inner hover:shadow-purple-700 rounded-full" />
                        </label>
                        <label>
                            Email:
                            <input type="email" value={email} onChange={e => setEmail(e.target.value)} className="block w-full mt-4 hover:drop-shadow-[0_0_0.1rem_#ffffff70] duration-400 p-2 md:p-1 text-center text-gray-300 md:text-[15px] hover:text-white border border-purple-400 shadow shadow-purple-950 hover:duration-300 hover:shadow-inner hover:shadow-purple-700 rounded-full" />
                        </label>
                    </div>
                    <button type="submit" className="block w-full mt-4 hover:drop-shadow-[0_0_0.1rem_#ffffff70] duration-400 p-2 md:p-1 text-center text-gray-300 md:text-[15px] hover:text-white border border-purple-400 shadow shadow-purple-950 hover:duration-300 hover:shadow-inner hover:shadow-purple-700 rounded-full">Register</button>
                </form>
            </div>
        </main>
    );
};

export default StudentRegister;