import React, { useState } from 'react';

const LoginForm: React.FC = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleUsernameChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setUsername(event.target.value);
  };

  const handlePasswordChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setPassword(event.target.value);
  };

  const handleSubmit = (event: React.FormEvent) => {
    event.preventDefault();
    console.log(`Username: ${username}, Password: ${password}`);
  };

  return (
    <main className="h-screen flex items-center justify-center">
      <div className='bg-gradient-to-b from-black from-75% to-violet-900 hover:duration-200 grid justify-items-center rounded-3xl py-6 md:py-5 shadow-md shadow-purple-600 border-[1px] hover:shadow-violet-500 hover:shadow-lg border-purple-950'>
        <h2 className="text-2xl m-1 md:m-0 font-bold hover:drop-shadow-[0_0_0.3rem_#ffffff70] text-gray-200 hover:duration-300 text-center duration-400">Sign In</h2>
        <form noValidate onSubmit={handleSubmit} className="space-y-2 md:space-y-1">
          <div className="text-sm">
            <label htmlFor="username" className="block">Email</label>
            <input type="text" name="Email" id="Email" placeholder="Email" value={username} onChange={handleUsernameChange} className="w-full md:h-full md:text-[15px] px-4 py-2 md:py-1 rounded-md border-gray-700 focus:border-transparent bg-black" />
          </div>
          <div className="text-sm">
            <label htmlFor="password" className="block">Password</label>
            <input type="password" name="password" id="password" placeholder="Password" value={password} onChange={handlePasswordChange} className="w-full md:h-full md:text-[15px] px-4 py-2 md:py-1 rounded-md border-gray-700 bg-black text-white focus:border-transparent" />
            <div className="flex justify-end py-1 hover:drop-shadow-[0_0_0.4rem_#ffffff70] text-xs text-gray-300">
              <a rel="noopener noreferrer" href="#">Forgot Password?</a>
            </div>
          </div>
          <button type="submit" className="block w-full hover:drop-shadow-[0_0_0.1rem_#ffffff70] duration-400 p-2 md:p-1 text-center text-gray-300 md:text-[15px] hover:text-white border border-purple-400 shadow shadow-purple-950 hover:duration-300 hover:shadow-inner hover:shadow-purple-700 rounded-full">Sign in</button>
        </form>
      </div>
    </main>
  );
};

export default LoginForm;
