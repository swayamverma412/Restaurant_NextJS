import { Inter } from "next/font/google";
import "./globals.css";
import Header from "@/components/Header/Header";
import Footer from "@/components/Footer/Footer";

const inter = Inter({ subsets: ["latin"] });

export const metadata = {
  title: "Create Next App",
  description: "Generated by create next app",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body
        className={`${inter.className} w-full flex flex-col items-center justify-start`}
      >
        <div id="portal-root"></div>
        <Header />
        {children}
        <Footer />
      </body>
    </html>
  );
}
